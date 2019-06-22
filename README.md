# InstaBoost

This repository is implementation of InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting on mmdetection. 

## Quick Start

1. Requirements  
We implement our method on Python 3.5. Other versions of Python 3.4+ should work with following packages:

```
Cython
opencv-python
Pillow
pycocotools
pytorch 1.0
scikit-image
scipy
```

2. Build matting module

```
cd mmdet/datasets
sh matting_init.sh
```

3. Install mmdetection according to [INSTALL.md](INSTALL.md)

4. Move the matting module, named like opencv_mat.cpython-35m-x86_64-linux-gnu.so, to where mmdetection package is installed. For example, I use conda to create an environment called 'mmtest', then I should move the module to 'PATH_TO_CONDA/anaconda3/envs/mmtest/lib/python3.5/site-packages/mmdet-0.6.0+53c647e-py3.5.egg/mmdet/datasets/AugSeg/global_matting'.

5. Train or test models according to [MMDET_README.md](MMDET_README.md)

## Configurations

Configurations for InstaBoost can be set up in [mmdet/datasets/AugSeg/config.py](mmdet/datasets/AugSeg/config.py). More details are shown in comments. 

## Acknowledgement

Our detection and instance segmentation framework is based on [mmdetecion](https://github.com/open-mmlab/mmdetection).