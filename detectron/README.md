# InstaBoost on detectron

Codes in this folder is an implementation of InstaBoost for detectron of [this version](https://github.com/roytseng-tw/Detectron.pytorch/tree/8315af319cd29b8884a7c0382c4700a96bf35bbc).

## Installation, training and testing

Prepare and run detectron according to [ORIREADME.md](ORIREADME.md).  

## Implementation

Since loading images and packaging annotations into roidb are in different stages in this code, implementing InstaBoost is a little complex. 

Main codes are in [lib/roi_data/minibatch.py](lib/roi_data/minibatch.py#L66L87). These codes mainly do three works, fetch image and annotations, InstaBoost, and package annotations into roidb. 

First two steps are easy to understand, while the third step might be confusing. We try to reuse `combined_roidb_for_training` function provided in [lib/datasets/roidb.py](lib/datasets/roidb.py#L37) to get new roidbs which are consistent with the previous ones. Therefore, we need to passing parameters `img_id`, `new_ann`, `coco` to infer a certain image and annotaion of the coco-style dataset we use before. We make a copy of lib/dataset folder, called lib/datasetAug, and changes some codes. Details are shown below.

[Line 8 - line 11](lib/roi_data/minibatch.py#L8-L11) in lib/roi_data/minibatch.py to import packages and load coco annotations. 

[Line 37](lib/datasetsAug/roidb.py#L37), [line 42](lib/datasetsAug/roidb.py#L42), [line 43](lib/datasetsAug/roidb.py#L43) and [line 63](lib/datasetsAug/roidb.py#L63) in lib/datasetsAug/roidb.py to pass parameter `coco`. 

[Line 56](lib/datasetsAug/json_dataset.py#L56), [line 70](lib/datasetsAug/json_dataset.py#L70), [line 89 - line 90](lib/datasetsAug/json_dataset.py#L89L90), [line 136 - line 142](lib/datasetsAug/json_dataset.py#L136L142), [line 147 - line 171](lib/datasetsAug/json_dataset.py#L147L171) and [line 222 - line 223](lib/datasetsAug/json_dataset.py#L222L223) in lib/datasetsAug/json_dataset.py to pass parameter `coco`, `img_id`, `new_ann` to replace these variables in original code. 


## Configurations

4x configurations are available in [InstaBoost_configs](InstaBoost_configs).

## Results and models

For your conveinience of evaluation and comparison, we report the evaluation number on COCO val below. In our paper, the numbers are obtained from test-dev.

|    InstaBoost   |     Network     |       Backbone       | Lr schd |      box AP       |      mask AP       |      Download       |
| :-------------: | :-------------: |      :--------:      | :-----: |      :----:       |      :-----:       | :-----------------: |
|    ×    |    Mask R-CNN   |       R-50-FPN       |   1x    |  37.7  |  33.7   | - |
|    √    |    Mask R-CNN   |       R-50-FPN       |   4x    |**40.3**|**35.7**|[Baidu](https://pan.baidu.com/s/1PSUFALTocC4axSjSbwqSjA) / [Google](https://drive.google.com/file/d/14183nkrToHkjXcWm14XUIQc7FgDDvb93/view?usp=sharing)|
|    ×    |    Mask R-CNN   |       R-101-FPN      |   1x    |  40.0  |  35.9   | - |
|    √    |    Mask R-CNN   |       R-101-FPN      |   4x    |**42.8**|**37.5**|[Baidu](https://pan.baidu.com/s/1JYA0MFUnNcWxPR8FfplFEw) / [Google](https://drive.google.com/file/d/1PPPJTl14VQj-LyA_cueDFHr8sibO2AQg/view?usp=sharing)|

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@article{Fang2019InstaBoost,
author = {Fang, Hao-Shu and Sun, Jianhua and Wang, Runzhong and Gou, Minghao and Li, Yong-Lu and Lu, Cewu},
title = {InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting},
journal={arXiv preprint arXiv:1908.07801},
year = {2019}
}
```
