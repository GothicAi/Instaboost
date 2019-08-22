# InstaBoost

This repository is implementation of ICCV2019 paper "InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting" on [mmdetection](https://github.com/open-mmlab/mmdetection) and [detectron](https://github.com/roytseng-tw/Detectron.pytorch) framework. Our paper has been released on arXiv https://arxiv.org/abs/1908.07801. 

## Common Settings and Quick Start

1. Requirements  
We implement our method on Python 3.5. To install InstaBoost, use this command. 

```
pip install InstaBoost
```

2. Install mmdetection according to [mmdetection/INSTALL.md](mmdetection/INSTALL.md). Train or test models according to [mmdetection/ORIREADME.md](mmdetection/ORIREADME.md). 

3. Prepare and run detectron according to [detectron/ORIREADME.md](detectron/ORIREADME.md).  

* Since these two frameworks may continue updating, codes in this repo may be a little different from [mmdetection](https://github.com/open-mmlab/mmdetection) and [detectron](https://github.com/roytseng-tw/Detectron.pytorch).

## Setup InstaBoost Configurations

To change InstaBoost Configurations, users can use function [`InstaBoostConfig`](https://github.com/GothicAi/InstaBoost-pypi#instaboostconfig).

## Model Zoo

Results and models are available in the [Model zoo](MODEL_ZOO.md). 

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@article{Fang2019InstaBoost,
author = {Fang, Hao-Shu and Sun, Jianhua and Wang, Runzhong and Gou, Minghao and Li, Yonglu and Lu, Cewu},
title = {InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting},
journal={arXiv preprint arXiv:1908.07801},
year = {2019}
}
```
Please also cite [mmdetection](https://github.com/open-mmlab/mmdetection) and [detectron](https://github.com/roytseng-tw/Detectron.pytorch) if you use the corresponding codes.


## Acknowledgement

Our detection and instance segmentation framework is based on [mmdetecion](https://github.com/open-mmlab/mmdetection) and [detectron](https://github.com/roytseng-tw/Detectron.pytorch).
