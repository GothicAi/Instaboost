import numpy as np
from copy import deepcopy
from .get_instance_group import extract
from .affine_transform import transform_image, transform_annotation
from .config import AugSegConfig
from .exceptions import *
import cv2
from .pointByHeatmap import paste_position
from PIL import Image, ImageEnhance, ImageOps, ImageFile


def get_new_data(ori_anns: list, ori_img: np.ndarray, config: AugSegConfig=None, background: np.ndarray=None):
    """
    Get a new image with new annotations from original image and annotations
    :param ori_anns: list of coco-style annotation dicts
    :param ori_img: numpy array
    :param config: a AugSegConfig instance. If None, the default parameters will be used.
    :param background: if not None, this background image will be used for augmentation
    :return: new_ann, new_img
    """
    ori_anns_bak = deepcopy(ori_anns)
    ori_anns = deepcopy(ori_anns)

    if len(ori_img.shape) == 2 or ori_img.shape[2] == 1:  # gray scale
        ori_img = cv2.merge([ori_img] * 3)

    if config is None:
        config = AugSegConfig()

    try:
        if background is None:
            background, instances_list, transforms_list, groupbnds_list, groupidx_list = \
                extract(ori_anns, ori_img, config)
        else:
            _, instances_list, transforms_list, groupbnds_list, groupidx_list = \
                extract(ori_anns, ori_img, config)
        assert background.shape == ori_img.shape, 'Background and original image shape mismatch'
        
        if config.heatmap_flag:
            heatmap_guided_pos_list = paste_position(ori_anns, ori_img, groupidx_list, groupbnds_list)
            for i in range(len(heatmap_guided_pos_list)):
                heatmap_guided_pos = heatmap_guided_pos_list[i]
       
                if heatmap_guided_pos[0] != -1:
                    transforms_list[i]['tx'] = heatmap_guided_pos[1]
                    transforms_list[i]['ty'] = heatmap_guided_pos[0]

        new_img = transform_image(background, instances_list, transforms_list)
        new_ann = transform_annotation(ori_anns, transforms_list, groupbnds_list, groupidx_list,
                                       background.shape[1], background.shape[0])
    except (AnnError, TrimapError):
        new_ann = ori_anns_bak
        new_img = ori_img

    color_flag = np.random.choice([0,1],p=[1-config.color_prob, config.color_prob])
    if color_flag:
        PIL_img = Image.fromarray(cv2.cvtColor(new_img,cv2.COLOR_BGR2RGB))
        PIL_img = randomColor(PIL_img)
        new_img = cv2.cvtColor(np.asarray(PIL_img),cv2.COLOR_RGB2BGR)

    return new_ann, new_img

def randomColor(image):
        """
        对图像进行颜色抖动
        :param image: PIL的图像image
        :return: 有颜色色差的图像image
        """
        random_factor = np.random.randint(0, 31) / 10.  # 随机因子
        color_image = ImageEnhance.Color(image).enhance(random_factor)  # 调整图像的饱和度
        random_factor = np.random.randint(10, 21) / 10.  # 随机因子
        brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  # 调整图像的亮度
        random_factor = np.random.randint(10, 21) / 10.  # 随机因子
        contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  # 调整图像对比度
        random_factor = np.random.randint(0, 31) / 10.  # 随机因子
        return ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  # 调整图像锐度
