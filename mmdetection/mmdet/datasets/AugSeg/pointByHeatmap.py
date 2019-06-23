'''
AugSeg:     input: (a list of coco style annotations, rgb numpy image)
            output: (a list of coco style annotations, rgb numpy image)



genmask -> mask:    generate total mask and each instance masks for one image
                    input: (a list of coco style annotations, img height int, img width int)
                    output: (a grey numpy mask on the certain img, a list of grey numpy masks, a list of centers of each obj)

genmask -> background:  generate background for one image
                        input: (rgb numpy image, grey numpy mask)
                        output: (rgb inpainted background)
                        method: opencv inpaint NS

genmask -> dilation:    generate three bounds for one instance
                        intput: (gery numpy mask, dilation kernel)
                        output: (three gery numpy masks)

genmask -> outline:     generate "trimap" for one instance
                        input: (four grey numpy masks)
                        output: (one grey numpy masks with five different depth)

genmask -> scale:   pick out middle scale instances

'''

import random
import numpy as np
import cv2
from pycocotools.coco import COCO
import pycocotools.mask as cocomask

from .help_functions import AnnError, cocoseg_to_binary, __get_coco_masks, getTrimap, getHeatpoint, getRings, normalize

def _get_mask_center_background(ann_list: list, img: np.ndarray, grouplist: list, bndlist: list):
    '''
    input: ann_list(list): a list of coco style annotations
           img(nd.array): image related to annotations
           grouplist(list): list of lists, one innner list [i,j,k] shows instances is crowd
           bndlist(list): list of bound boxes for grouped instances

    output: background(nd.array): an rgb background
            mask_list(list): a list of single_mask, single_mask is an nd.array of an instance, 
            center_list(list): a list of group_center, group_center is a list indicates the center of grouped instance
    '''
    single_mask_list = []
    center_list = []
    mask_list = []

    for ann in ann_list:
        single_mask, _ = __get_coco_masks([ann], img)
        single_mask_list.append(single_mask)
    
    for group in grouplist:
        group_mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)
        for idx in group:
            group_mask[single_mask_list[idx] > 0] = 255
        mask_list.append(group_mask)

    for bbox in bndlist:
        group_center = [(bbox[0]+bbox[2])/2, (bbox[1]+bbox[3])/2]
        center_list.append(group_center)

    img_mask, _ = __get_coco_masks(ann_list, img)
    kernel = np.ones((5, 5),np.uint8)
    img_mask = cv2.dilate(img_mask.astype(np.float64), kernel, iterations = 2)
    background = cv2.inpaint(img, np.uint8(img_mask), 5, cv2.INPAINT_NS)

    return background, mask_list, center_list


def _get_trimap(single_mask: np.ndarray, kernel_size: int=5):
    '''
    input: single_mask(np.ndarray): a mask of an instance
           kernel_size(int): dilation kernel size

    output: trimap(np.ndarray): one grey numpy masks with five different depth
                                out -> in: 0, 1, 2, 3, 0
    '''
    mask_list = [single_mask]
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    trimap = np.zeros((single_mask.shape[0], single_mask.shape[1]), dtype=np.int32)

    for i in range(1, 4):
        mask_list.append(cv2.dilate(single_mask.astype(np.float64), kernel, iterations = i*2))

    for i in range(3, -1, -1):
        trimap[mask_list[i] > 200] = 4 - i # out -> in: 0, 1, 2, 3, 0

    return trimap

def _get_paste_pos(image: np.ndarray, background: np.ndarray, trimap: np.ndarray, center: list, shrink: int=10, ratio: float=0.4):
    '''
    input: image(np.ndarray): original rgb image
           background(np.ndarray): clear all instances background
           trimap(np.ndarray): out -> in: 0, 1, 2, 3, 0
           center(list): center pos
           shrink(int): shrink scale
           ratio(float): ratio to choose larger than 200
    
    output: pos(tuple): (int, int) position to paste on the background
    '''
    orishape = image.shape[:2]
    desshape = (int(image.shape[0]/shrink), int(image.shape[1]/shrink))
    image = cv2.resize(image, (desshape[1], desshape[0]))
    background = cv2.resize(background, (desshape[1], desshape[0]))
    trimap = cv2.resize(trimap.astype(np.uint8), (desshape[1], desshape[0]))
    oripos = [int(center[1]/shrink), int(center[0]/shrink)]

    heatmap = np.zeros((image.shape[0], image.shape[1]), dtype=np.float32)
    oriTrimap = getTrimap(trimap)
    oriRings = getRings(image, oriTrimap)
    res = []
    for i in range(background.shape[0]):
        for j in range(background.shape[1]):
            heatPoint = getHeatpoint(oriTrimap, oriRings, background, oripos, [i, j], config=[0.25, 0.35, 0.4])
            res.append([i,j,heatPoint])
    for point in res:
        heatmap[point[0]][point[1]] = point[2]
    heatmap = normalize(heatmap)
    heatmap = cv2.resize(heatmap, (orishape[1], orishape[0]))

    poses = np.stack(np.where(heatmap>200), axis=1)
    if random.random() < ratio or len(poses)==0:
        poses = np.stack(np.where(heatmap>150), axis=1)

    if len(poses)==0:
        return np.array([-1, -1])

    choice = np.random.choice(range(len(poses)))
    pos = poses[choice]

    return pos

def paste_position(anns, img, grouplist, bndlist):
    heatmap_guided_pos_list = []

    background, mask_list, center_list = _get_mask_center_background(anns, img, grouplist, bndlist)
    for i in range(len(mask_list)):
        trimap = _get_trimap(mask_list[i])
        pos = _get_paste_pos(img, background, trimap, center_list[i], 10)
        heatmap_guided_pos_list.append(pos)

    return heatmap_guided_pos_list

if __name__ == '__main__':
    import time
    coco = COCO('annotations/instances_val2017.json')
    ImgIds = coco.getImgIds()
    ImgIds.sort()

    for ImgId in ImgIds[:10]:
        filename = coco.loadImgs(ImgId)[0]['file_name']
        annIds = coco.getAnnIds(imgIds=[ImgId], iscrowd=None)
        anns = coco.loadAnns(annIds)
        img = cv2.imread("val2017/"+filename)

        background, mask_list, center_list = _get_mask_center_background(anns, img)
        for i in range(len(mask_list)):
            trimap = _get_trimap(mask_list[i])
            pos = _get_paste_pos(img, background, trimap, center_list[i], 10)
            print(pos)
