#train
CUDA_VISIBLE_DEVICES=4,5,6,7 python3 tools/train_net_step.py --dataset coco2017 --cfg configs/baselines/e2e_mask_rcnn_R-50-FPN_1x.yaml --use_tfboard  --nw 56

#test
#python3 tools/test_net.py --dataset coco2017 --cfg configs/baselines/e2e_mask_rcnn_R-50-FPN_1x.yaml --load_ckpt {path/to/your/checkpoint}
