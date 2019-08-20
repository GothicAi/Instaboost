# InstaBoost on mmdetection

Codes in this folder is an implementation of InstaBoost for detectron of [this version](https://github.com/roytseng-tw/Detectron.pytorch/tree/8315af319cd29b8884a7c0382c4700a96bf35bbc).

## Implementation



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