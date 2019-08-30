# InstaBoost on yolact

Codes in this folder is an implementation of InstaBoost for yolact of [this version](https://github.com/dbolya/yolact/tree/29e809e563d0c3e6c47c5c6716b8cc81686a2b24).

## Installation, training and testing

Prepare and run yolact according to [ORIGINAL_README.md](ORIGINAL_README.md).  
Besides, InstaBoost should be installed before running the code. 
We suggest using pip to install InstaBoost.

``` shell
pip install instaboost 
```

## Implementation

Integrating InstaBoost into yolact is quite simple.
Only few lines should be modified to put InstaBoost into use.

[data/coco.py](data/coco.py), [train.py](train.py) and [eval.py](eval.py) should be changed.
  
[coco.py/line 11](data/coco.py#L11) imports InstaBoost.

[coco.py/line 68](data/coco.py#L68) assigns the value of `is_train`.

[coco.py/line 116-121](data/coco.py#L116-L121) These lines are originally located at [line 139-146](data/coco.py#L137-L144). They are put here because the InstaBoost function `get_new_data` needs both the annotation and the image.

[coco.py/line 123-124](data/coco.py#L123-L124) checks if it's training or evaluating. When training, the program runs the InstaBoost function and gets new image and annotation. Both the variables `target` and `img` are acquired using the official COCO Python API.

[train.py/line 134](train.py#L134) and [train.py/line 140](train.py#L140) assign `True` to the variable of `is_train`.

[eval.py/line 1006](eval.py#L1006) assigns `False` to the variable of `is_train`.
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
