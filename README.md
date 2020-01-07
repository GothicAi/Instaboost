# InstaBoost

This repository is implementation of ICCV2019 paper "InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting". Our paper has been released on arXiv https://arxiv.org/abs/1908.07801. 

## Install InstaBoost

### Easy install version
***Note: If you cannot install instaboost successfully using conda, we provide a simpler instaboost that do not need matting. The final results is 0.1 mAP lower than the original one, but we highly recommend it.***
```
pip install instaboostfast
# in python
>>> import instaboostfast as instaboost
```

### Original version
To install original InstaBoost, use this command.  *If you successfully install and import it in python, you are really lucky!*

```
pip install instaboost
```
We strongly recommend install it using conda

```
conda create -n instaboost python=3.6
conda activate instaboost
conda install -c salilab opencv-nopython        # opencv2
conda install -c serge-sans-paille gcc_49       # you need to use conda's gcc instead of system's
ln -s ~/miniconda3/envs/instaboost/bin/g++-4.9 ~/miniconda3/envs/instaboost/bin/g++   #link to bin
ln -s ~/miniconda3/envs/instaboost/bin/gcc-4.9 ~/miniconda3/envs/instaboost/bin/gcc   #link to bin
pip install cython numpy
pip install opencv-mat
pip install instaboost
```

The detail implementation can be found [`here`](https://github.com/GothicAi/InstaBoost-pypi).

***Because InstaBoost depends on matting package [here](https://github.com/GothicAi/cython-global-matting), we highly recommend users to use python3.5 or 3.6, OpenCV 2.4 to avoid some errors. Envrionment setting instructions can be found [here](https://github.com/GothicAi/cython-global-matting#environment-settings-linux).***



## Quick Start

Video demo for InstaBoost: https://www.youtube.com/watch?v=iFsmmHUGy0g

* **News:** InstaBoost is now officially supported in [mmdetection](https://github.com/open-mmlab/mmdetection)!

Currently we have integrated InstaBoost into three open implementations: [mmdetection](https://github.com/open-mmlab/mmdetection), [detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [yolact](https://github.com/dbolya/yolact).

* **mmdetection:** Checkout [mmdetection](mmdetection).  

* **detectron:** Checkout [detectron](detectron). 

* **yolact:** Checkout [yolact](yolact)

*Since these frameworks may continue updating, codes in this repo may be a little different from their current repo.*

## Use InstaBoost In Your Project

It is easy to integrate InstaBoost into your framework. You can refer to instructions of our implementations on [mmdetection](mmdetection#implementation), [detectron](detectron#implementation) and [yolact](yolact#implementation)

## Setup InstaBoost Configurations

To change InstaBoost Configurations, users can use function [`InstaBoostConfig`](https://github.com/GothicAi/InstaBoost-pypi#instaboostconfig).

## Model Zoo

Results and models are available in the [Model zoo](MODEL_ZOO.md).  More models are coming!

## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@inproceedings{fang2019instaboost,
  title={Instaboost: Boosting instance segmentation via probability map guided copy-pasting},
  author={Fang, Hao-Shu and Sun, Jianhua and Wang, Runzhong and Gou, Minghao and Li, Yong-Lu and Lu, Cewu},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={682--691},
  year={2019}
}
```
Please also cite [mmdetection](https://github.com/open-mmlab/mmdetection), [detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [yolact](https://github.com/dbolya/yolact) if you use the corresponding codes.


## Acknowledgement

Our detection and instance segmentation framework is based on [mmdetecion](https://github.com/open-mmlab/mmdetection), [detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [yolact](https://github.com/dbolya/yolact).
