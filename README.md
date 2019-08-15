# InstaBoost

This repository is implementation of InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting on [mmdetecion](https://github.com/open-mmlab/mmdetection) and [detectron](https://github.com/roytseng-tw/Detectron.pytorch). 

## MMdetection Framework Quick Start

1. Enter 'mmdetection/' folder. 

2. Requirements  
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

3. Build matting module

```
cd mmdet/datasets
sh matting_init.sh
```

4. Install mmdetection according to [mmdetection/INSTALL.md](mmdetection/INSTALL.md). 

5. Move the matting module, named like opencv_mat.cpython-35m-x86_64-linux-gnu.so, to where mmdetection package is installed. For example, I use conda to create an environment called 'mmtest', then I should move the module to 'PATH_TO_CONDA/anaconda3/envs/mmtest/lib/python3.5/site-packages/mmdet-0.6.0+53c647e-py3.5.egg/mmdet/datasets/AugSeg/global_matting'.

6. Train or test models according to [mmdetection/README.md](mmdetection/README.md). 

## Detectron Framework Quick Start

1. Enter 'detectron/' folder. 

2. Requirements  
We implement our method on Python 3.5. Besides packages shown in [detectron/README.md](detectron/README.md), following packages are also needed:

```
Pillow
scikit-image
scipy
```

3. Build matting module

```
cd detectron/lib
sh matting_init.sh
```

4. Prepare and run detectron according to [detectron/README.md](detectron/README.md). 


## Configurations

Configurations for InstaBoost can be set up in [mmdet/datasets/AugSeg/config.py](mmdetection/mmdet/datasets/AugSeg/config.py) and [detectron/lib/AugSeg/config.py](detectron/lib/AugSeg/config.py). More details are shown in comments. 

## Acknowledgement

Our detection and instance segmentation framework is based on [mmdetecion](https://github.com/open-mmlab/mmdetection) and [detectron](https://github.com/roytseng-tw/Detectron.pytorch).