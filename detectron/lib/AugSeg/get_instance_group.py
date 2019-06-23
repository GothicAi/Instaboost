import matplotlib
matplotlib.use('AGG')
    
import numpy as np
import cv2
import pycocotools.mask as cocomask
from scipy import ndimage
from .global_matting import global_matting, guided_filter
from .single_image_process import get_transform, get_restriction
from .exceptions import *
from .config import AugSegConfig


def cocoseg_to_binary(seg, height, width):
    """
    COCO style segmentation to binary mask
    :param seg: coco-style segmentation
    :param height: image height
    :param width: image width
    :return: binary mask
    """
    if type(seg) == list:
        rle = cocomask.frPyObjects(seg, height, width)
        rle = cocomask.merge(rle)
        mask = cocomask.decode([rle])
    elif type(seg['counts']) == list:
        rle = cocomask.frPyObjects(seg, height, width)
        mask = cocomask.decode([rle])
    else:
        rle = cocomask.merge(seg)
        mask = cocomask.decode([rle])
    assert mask.shape[2] == 1
    return mask[:, :, 0]


def __get_coco_masks(anns: list, height: int, width: int):
    """
    Get coco masks from annotations.
    :param anns: list of coco-style annotation
    :param height: image height
    :param width: image width
    :return: masks, hxw numpy array
             classes, nx1
    """
    if len(anns) == 0:
        raise AnnError('Empty annotation detected.')
    
    classes = []
    mask = np.zeros((height, width), dtype=np.int32)
    
    for inst_idx, ann in enumerate(anns):
        cat_id = ann['category_id']
        classes.append(cat_id)

        m = cocoseg_to_binary(ann['segmentation'], height, width)  # zero one mask
        m = m.astype(np.int32) * (inst_idx + 1)
        mask[m > 0] = m[m > 0]

    classes = np.asarray(classes)
    return mask, classes
    
    
def overlap(bbox1, bbox2):
    """
    Given two bboxes, return whether the two bboxes overlap
    """
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2
    return (x1 < x2 + w2) and (y1 < y2 + h2) and (x2 < x1 + w1) and (y2 < y1 + h1)
    

def dfs(bboxs, belonging, cur_group, group_idx, i):
    """
    Depth first search (dfs) finding overlapped instance groups.
    :param bboxs: list of bounding boxes
    :param belonging: list of instance belongings
    :param cur_group: current group list
    :param group_idx: current group index
    :param i: current instance index
    """
    numinst = len(bboxs)
    for j in range(numinst):
        if belonging[j] == 0 and j != i:
            if overlap(bboxs[i],bboxs[j]):
                belonging[j] = group_idx
                cur_group.append(j)
                dfs(bboxs, belonging, cur_group, group_idx, j)


def gettrimap(mask, k):
    """
    Compute matting trimap from given mask.
    :param mask: binary ground truth mask
    :param k: number of extended pixels
    :return: matting trimap. 255 for groundtruth foreground, 127 for uncertain area, 0 for ground truth background
    """
    #np.set_printoptions(threshold=np.nan)
    kernel = np.ones((2 * k + 1, 2 * k + 1), dtype=np.int32)
    trimap = ndimage.convolve(mask, kernel, mode='constant')

    trimap = (trimap > 0) * 127
    trimap[mask > 0] = 255

    if trimap.max() != 255 or trimap.min() != 0:
        raise TrimapError('matting trimap failed.')
    return trimap.astype(np.uint8)


def get_masks(mat, klist):
    """
    Merge the mask of multiple objects in klist.
    """
    retMat = np.zeros_like(mat)
    for k in klist:
        retMat += (mat - 1 == k).astype(np.uint8)
    return retMat
    

def extract(anns: list, img: np.ndarray, config: AugSegConfig):
    """
    Inpaint background, extract list of instances (in overlapping groups), get transformations and other useful
    information from input image and annotations.
    :param anns: list of input annotations
    :param img: input original image
    :param config: an AugSegConfig instance containing transform parameters
    :return: [background: inpainted background image
              instances_list: list of instance rgba images
              transforms_list: list of transformation dicts
              groupbnd_list: list of bounding boxes
              group: list of instence indices in groups]
    """
    width = img.shape[1]
    height = img.shape[0]

    mask, labels = __get_coco_masks(anns, height, width)

    # inpainting
    #inpaint_mask = np.uint8(mask > 0)
    #inpaint_mask = ndimage.binary_dilation(inpaint_mask, structure=ndimage.generate_binary_structure(2, 2), iterations=2)
    background = cv2.inpaint(img, np.uint8(mask), 5, cv2.INPAINT_NS)

    numinst = len(anns)
    bboxs = [ann['bbox'] for ann in anns]

    inst_group_belonging = [0] * numinst
    group = []
    group_idx = 1
    for i in range(numinst):
        if inst_group_belonging[i] == 0:
            group.append([i])
            inst_group_belonging[i] = group_idx
            dfs(bboxs, inst_group_belonging, group[len(group) - 1], group_idx, i)
            group_idx += 1
    realbboxs = []

    instances_list = []
    transforms_list = []
    groupbnd_list = []
    for i in range(len(group)):
        x, y, w, h = bboxs[group[i][0]]
        realbboxs.append([x, y, x + w, y + h])
        for j in range(len(group[i])):
            x, y, w, h = bboxs[group[i][j]]
            realbboxs[i][0] = min(realbboxs[i][0], x)
            realbboxs[i][1] = min(realbboxs[i][1], y)
            realbboxs[i][2] = max(realbboxs[i][2], x + w)
            realbboxs[i][3] = max(realbboxs[i][3], y + h)
            xmin, ymin, xmax, ymax = realbboxs[i]

        maskgroupi = get_masks(mask, group[i])
        trimapi = gettrimap(maskgroupi, 5)

        alphamapi = global_matting(img, trimapi)
        alphamapi = guided_filter(img, trimapi, alphamapi, 10, 1e-5)

        ymin, ymax, xmin, xmax = [int(round(x)) for x in (ymin, ymax, xmin, xmax)]
        resulti = np.dstack((img[ymin:ymax, xmin:xmax], alphamapi[ymin:ymax, xmin:xmax]))

        restricts = get_restriction([xmin, ymin, xmax, ymax], width, height)
        resulti, transformi = get_transform(resulti, restricts, config) # resulti may be flipped

        transformi['tx'] += (xmin + xmax) / 2
        transformi['ty'] += (ymin + ymax) / 2

        instances_list.append(resulti)
        transforms_list.append(transformi)
        groupbnd_list.append([xmin, ymin, xmax, ymax])

    return background, instances_list, transforms_list, groupbnd_list, group
