# InstaBoost on mmdetection

Codes in this folder is an implementation of InstaBoost for [mmdetection v0.6.0](https://github.com/open-mmlab/mmdetection/tree/v0.6.0).

## Implementation

Users can simply implement InstaBoost on mmdetection framework by changing [codes](mmdet/datasets/custom.py#L188L199) in [mmdet/datasets/custom.py](mmdet/datasets/custom.py), after import InstaBoost [here](mmdet/datasets/custom.py#L13).

The reason for modifying these codes is `get_new_data` function need variable `img` as input. Thus, `get_ann_info` function need to be expand by deleting
```
ann = self.get_ann_info(idx)
```
and adding
```
        img_id = self.img_infos[idx]['id']
        ann_ids = self.coco.getAnnIds(imgIds=[img_id])
        ann_info = self.coco.loadAnns(ann_ids)

        aug_flag = np.random.choice([0,1],p=[0.5,0.5])
        if aug_flag:
            ann_info, img = get_new_data(ann_info, img, None, background=None)

        ann = self._parse_ann_info(ann_info, self.with_mask)
```

## Configurations

4x configurations are available in [mmdet/InstaBoost_configs](mmdet/InstaBoost_configs).

## Results and models

For your conveinience of evaluation and comparison, we report the evaluation number on COCO val below. In our paper, the numbers are obtained from test-dev.

|    InstaBoost   |     Network     |       Backbone       | Lr schd |      box AP       |      mask AP       |      Download       |
| :-------------: | :-------------: |      :--------:      | :-----: |      :----:       |      :-----:       | :-----------------: |
|   ×   |    Mask R-CNN   |   X-101-64x4d-FPN    |   1x    |  42.1  |  38.0   | - |
|   √   |    Mask R-CNN   |   X-101-64x4d-FPN    |   4x    |  44.5  |  39.5   |[Baidu](https://pan.baidu.com/s/1KrHQBHcHjWONpXbC2qUzxw) / [Google](https://drive.google.com/file/d/1qD4V9uYbtpaZBmTMTgP7f0uw46zroY9-/view?usp=sharing)|
|   ×   |  Cascade R-CNN  |       R-101-FPN      |   1x    |  42.6  |  37.0   | - |
|   √   |  Cascade R-CNN  |       R-101-FPN      |   4x    |  45.4  |  39.2   |[Baidu](https://pan.baidu.com/s/1_4cJ0B9fugcA-oBHYe9o_A) / [Google](https://drive.google.com/file/d/1xhiuFoOMQyDIvOrz6MiAZPboRRe1YK8p/view?usp=sharing)|
|   ×   |  Cascade R-CNN  |   X-101-64x4d-FPN    |   1x    |  45.4  |  39.1   | - |
|   √   |  Cascade R-CNN  |   X-101-64x4d-FPN    |   4x    |  47.2  |  40.4   |[Baidu](https://pan.baidu.com/s/1nu73IpRbTEb4caPMHWJMXA) / [Google](https://drive.google.com/file/d/11iaKH-ZeVCi-65wzlT5OxxUOkREMzXRW/view?usp=sharing)|


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

If you use this version of mmdetection, please also citing their original repo:

```
@article{mmdetection,
  title   = {{MMDetection}: Open MMLab Detection Toolbox and Benchmark},
  author  = {Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and
             Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and
             Liu, Ziwei and Xu, Jiarui and Zhang, Zheng and Cheng, Dazhi and
             Zhu, Chenchen and Cheng, Tianheng and Zhao, Qijie and Li, Buyu and
             Lu, Xin and Zhu, Rui and Wu, Yue and Dai, Jifeng and Wang, Jingdong
             and Shi, Jianping and Ouyang, Wanli and Loy, Chen Change and Lin, Dahua},
  journal= {arXiv preprint arXiv:1906.07155},
  year={2019}
}
```
