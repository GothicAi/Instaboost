# InstaBoost on mmdetection

Codes in this folder is an implementation of InstaBoost for detectron of [this version](https://github.com/roytseng-tw/Detectron.pytorch/tree/8315af319cd29b8884a7c0382c4700a96bf35bbc).

## Implementation

Since loading images and packaging annotations into roidb are in different stages in this code, implementing InstaBoost is a little complex. 

Main codes are in [lib/roi_data/minibatch.py](lib/roi_data/minibatch.py#L66L87). These codes do mainly do three works, fetch image and annotations, InstaBoost, and package annotations inot roidb. 

First two steps are easy to understand, while the third step might be confusing. We try to use `combined_roidb_for_training` function provided in [lib/datasets/roidb.py](lib/datasets/roidb.py#L37) to get new roidbs which are consistent with the previous ones. Therefore, we need to passing parameters `img_id`, `new_ann`, `coco` to infer a certain image and annotaion of the coco-style dataset we use before. We make a copy of lib/dataset folder, called lib/datasetAug, and changes some codes. Details are shown below.



## Configurations

4x configurations are available in [detectron/InstaBoost_configs](detectron/InstaBoost_configs).

## Results and models

|    InstaBoost   |     Network     |       Backbone       | Lr schd |      box AP       |      mask AP       |      Download       |
| :-------------: | :-------------: |      :--------:      | :-----: |      :----:       |      :-----:       | :-----------------: |
|    ×    |    Mask R-CNN   |       R-50-FPN       |   1x    |  37.7  |  33.7   | - |
|    √    |    Mask R-CNN   |       R-50-FPN       |   4x    |  40.3  |  35.7   |[Baidu](https://pan.baidu.com/s/1PSUFALTocC4axSjSbwqSjA) / [Google](https://drive.google.com/file/d/14183nkrToHkjXcWm14XUIQc7FgDDvb93/view?usp=sharing)|
|    ×    |    Mask R-CNN   |       R-101-FPN      |   1x    |  40.0  |  35.9   | - |
|    √    |    Mask R-CNN   |       R-101-FPN      |   4x    |  42.8  |  37.5   |[Baidu](https://pan.baidu.com/s/1JYA0MFUnNcWxPR8FfplFEw) / [Google](https://drive.google.com/file/d/1PPPJTl14VQj-LyA_cueDFHr8sibO2AQg/view?usp=sharing)|

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@inproceedings{Fang2019InstaBoost,
author = {Fang, Hao-Shu and Sun, Jianhua and Wang, Runzhong and Gou, Minghao and Li, Yonglu and Lu, Cewu},
title = {InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting},
booktitle = {ICCV},
year = {2019}
}
```