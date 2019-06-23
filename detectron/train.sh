srun --partition=Segmentation --job-name=mix --gres=gpu:8 python tools/train_net_step.py --dataset coco2017 --cfg configs/baselines/e2e_mask_rcnn_R-50-FPN_1x.yaml --use_tfboard  --nw 32
