import numpy as np
import pycocotools.mask as cocomask
from copy import deepcopy

class AnnError(Exception):
    """
    Error with Input annotation.
    """
    def __init__(self, err):
        super(AnnError, self).__init__(err)

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

def __get_coco_masks(anns: list, img):
    """
    Get coco masks from annotations.
    :param anns: list of coco-style annotation
    :param height: image height
    :param width: image width
    :return: masks, hxw numpy array
             classes, nx1
    """
    width = img.shape[1]
    height = img.shape[0]

    if len(anns) == 0:
        raise AnnError('Empty annotation detected.')
    
    classes = []
    mask = np.zeros((height, width), dtype=np.int32)
    
    for inst_idx, ann in enumerate(anns):
        cat_id = ann['category_id']
        classes.append(cat_id)

        m = cocoseg_to_binary(ann['segmentation'], height, width)  # zero one mask
        m = m.astype(np.int32) * (inst_idx + 1)
        mask[m > 0] = 255

    classes = np.asarray(classes)
    return mask, classes

def getTrimap(outline):
    # out -> in: 0, 1, 2, 3, 0
    trimap = [] #从左到右是从外到内
    for i in range(1, 4, 1):
        trimap.append(np.stack(np.where(outline==i), axis=1))
    return trimap


def translateTrimap(trimap, oripos, augpos):
    augTrimap = deepcopy(trimap)
    oripos = np.array(oripos)
    for k in range(3):
        augTrimap[k] = trimap[k] - oripos + augpos
    return augTrimap


def getRings(img, trimap):
    width = img.shape[0]
    height = img.shape[1]

    rings = []
    for i in range(3):
        x, y = trimap[i][:, 0], trimap[i][:, 1]
        posflag = (x < width) * (x >= 0) * (y < height) * (y >= 0)
        if posflag.all():
            rings.append(img[x, y])
        else:
            return []
    return rings


def cosine_similarity(vector1, vector2):
    return np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))


def Euclidean_Distance(vector1, vector2):
    return np.sum(np.sqrt(np.sum(np.square(vector1-vector2), axis=1)))


def getHeatpoint(oriTrimap, oriRings, background, oripos, augpos, config=[0.25, 0.35, 0.4]):
    augTrimap = translateTrimap(oriTrimap, oripos, augpos)
    augRings = getRings(background, augTrimap)
    if not augRings:
        return -1

    heatPoint = 0
    for i in range(3):
        matori = oriRings[i].astype(int)
        mataug = augRings[i].astype(int)
        ed = Euclidean_Distance(matori, mataug)/255
        heatPoint += config[i]*ed
    return heatPoint

def normalize(heatmap):
    mm = np.max(heatmap[heatmap>=0])
    heatmap[heatmap<0] = mm
    #heatmap[heatmap<400] = (heatmap[heatmap<400]/20)**2
    #heatmap = -np.log(heatmap/mm)
    heatmap =  (1-heatmap/mm)**3
    mm = np.max(heatmap)
    heatmap = heatmap/mm *255
    return heatmap
