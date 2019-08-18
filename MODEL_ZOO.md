# Model Zoo

## Common settings
 - All models were trained on `coco_2017_train`, and tested on the `coco_2017_val`.
 - To balance accuracy and training time when using InstaBoost, models released in this page are all trained for 48 Epochs. Other training and testing configs are strictly following the original framework. 

## Baselines

|    Framework    |     Network     |       Backbone       | Lr schd |      box AP       |      mask AP       |      Download       |
| :-------------: | :-------------: |      :--------:      | :-----: |      :----:       |      :-----:       | :-----------------: |
|    Detectron    |    Mask R-CNN   |       R-50-FPN       |   4x    |  40.3(orig:37.7)  |  35.7(orig:33.7)   |[Baidu](https://pan.baidu.com/s/1PSUFALTocC4axSjSbwqSjA) | [Google](https://drive.google.com/file/d/14183nkrToHkjXcWm14XUIQc7FgDDvb93/view?usp=sharing)|
|    Detectron    |    Mask R-CNN   |       R-101-FPN      |   4x    |  42.8(orig:40.0)  |  37.5(orig:35.9)   |[Baidu](https://pan.baidu.com/s/1JYA0MFUnNcWxPR8FfplFEw) | [Google](https://drive.google.com/file/d/1PPPJTl14VQj-LyA_cueDFHr8sibO2AQg/view?usp=sharing)|
|   MMdetection   |    Mask R-CNN   |   X-101-64x4d-FPN    |   4x    |  44.5(orig:42.1)  |  39.5(orig:38.0)   |[Baidu](https://pan.baidu.com/s/1KrHQBHcHjWONpXbC2qUzxw) | [Google](https://drive.google.com/file/d/1qD4V9uYbtpaZBmTMTgP7f0uw46zroY9-/view?usp=sharing)|
|   MMdetection   |  Cascade R-CNN  |       R-101-FPN      |   4x    |  45.4(orig:42.6)  |  39.2(orig:37.0)   |[Baidu](https://pan.baidu.com/s/1_4cJ0B9fugcA-oBHYe9o_A) | [Google](https://drive.google.com/file/d/1xhiuFoOMQyDIvOrz6MiAZPboRRe1YK8p/view?usp=sharing)|
|   MMdetection   |  Cascade R-CNN  |   X-101-64x4d-FPN    |   4x    |  47.2(orig:45.4)  |  40.4(orig:39.1)   |[Baidu](https://pan.baidu.com/s/1nu73IpRbTEb4caPMHWJMXA) | [Google](https://drive.google.com/file/d/11iaKH-ZeVCi-65wzlT5OxxUOkREMzXRW/view?usp=sharing)|
