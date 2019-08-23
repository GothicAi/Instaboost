# InstaBoost on yolact

Codes in this folder is an implementation of InstaBoost for yolact of [this version](https://github.com/dbolya/yolact).

## Installation, training and testing

Prepare and run yolact according to [ORIGINAL_README.md](ORIGINAL_README.md).  
Besides, InstaBoost should be installed before running the code. 
We suggest using pip to install InstaBoost.

``` shell
pip install InstaBoost 
```

## Implementation

Integrating InstaBoost into yolact is quite simple.
Only few lines should be modified to put InstaBoost into use.

Only [data/coco.py](data/coco.py) should be changed.
  
[line 11](data/coco.py#L11) Importing InstaBoost.

[line 115-120](data/coco.py#L115-L120) These lines are originally located at [line 137-144](data/coco.py#L137-L144). They are put here because the InstaBoost function `get_new_data` needs both the annotation and the image.

[line 122](data/coco.py#L122) Run the InstaBoost function and get new image and annotation. Both the variables `target` and `img` are acquired using the official COCO Python API.


## Results and models

For your conveinience of evaluation and comparison, we report the evaluation number on COCO val below. In our paper, the numbers are obtained from test-dev.

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
