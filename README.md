# InstaBoost

This repository is implementation of ICCV2019 paper "InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting". Our paper has been released on arXiv https://arxiv.org/abs/1908.07801. 

## Install InstaBoost

1. Requirements  
We implement our method on Python 3.5. To install InstaBoost, use this command. 

```
pip install instaboost
```

The detail implementation can be found [`here`](https://github.com/GothicAi/InstaBoost-pypi).

## Quick Start

Currently we have integrated InstaBoost into three open implementations: [mmdetection](https://github.com/open-mmlab/mmdetection), [detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [yolact](https://github.com/dbolya/yolact).

* **mmdetection:** Checkout [mmdetection](mmdetection).  

* **detectron:** Checkout [detectron](detectron). 

* **yolact:** Checkout [yolact](yolact)

*Since these frameworks may continue updating, codes in this repo may be a little different from their current repo.*

## Use InstaBoost In Your Project

It is easy to integrate InstaBoost into your framework. You can refer to instructions of our implementations [here](mmdetection#implementation), [here](detectron#implementation) and [here](yolact#implementation)

## Setup InstaBoost Configurations

To change InstaBoost Configurations, users can use function [`InstaBoostConfig`](https://github.com/GothicAi/InstaBoost-pypi#instaboostconfig).

## Model Zoo

Results and models are available in the [Model zoo](MODEL_ZOO.md).  More models are coming!

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
Please also cite [mmdetection](https://github.com/open-mmlab/mmdetection), [detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [yolact](https://github.com/dbolya/yolact) if you use the corresponding codes.


## Acknowledgement

Our detection and instance segmentation framework is based on [mmdetecion](https://github.com/open-mmlab/mmdetection), [detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [yolact](https://github.com/dbolya/yolact).
