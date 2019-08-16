# Model Zoo

## Common settings
 - All models were trained on `coco_2017_train`, and tested on the `coco_2017_val`.
 - To balance accuracy and training time when using InstaBoost, models released in this page are all trained for 48 Epochs. Other training and testing configs are strictly following the original framework. 

## Baselines

|    Framework    |     Network     |       Backbone       | Lr schd | box AP | mask AP |      Download       |
| :-------------: | :-------------: |      :--------:      | :-----: | :----: | :-----: | :-----------------: |
|    Detectron    |    Mask R-CNN   |       R-50-FPN       |   4x    |  40.3  |  35.7   |      [model]()      |
|    Detectron    |    Mask R-CNN   |       R-101-FPN      |   4x    |  42.8  |  37.5   |      [model]()      |
|   MMdetection   |    Mask R-CNN   |   X-101-64x4d-FPN    |   4x    |  44.5  |  39.5   |      [model]()      |
|   MMdetection   |  Cascade R-CNN  |       R-101-FPN      |   4x    |  45.4  |  39.2   |      [model]()      |
|   MMdetection   |  Cascade R-CNN  |   X-101-64x4d-FPN    |   4x    |  47.2  |  40.4   |      [model]()      |