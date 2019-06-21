srun -p AD --job-name=mmdet --gres=gpu:8 python tools/train.py configs/cascade_mask_rcnn_r50_fpn_1x.py --gpus 8
