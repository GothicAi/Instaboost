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

4x configurations are in [mmdet/InstaBoost_configs](mmdet/InstaBoost_configs).

## Results and models

Some results can be seen in [MODEL_ZOO](https://github.com/GothicAi/Instaboost/blob/master/MODEL_ZOO.md).

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