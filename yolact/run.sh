#!/bin/bash
#SBATCH -J yolact
#SBATCH -p gpu
#SBATCH -N 1
#SBATCH --output=log.%j.out
#SBATCH --error=log.%j.err
#SBATCH -t 10:00:00
#SBATCH --gres=gpu:2
module load python/3.7.1
module load cuda/10.0
module load cudnn/7.4.2
source ~/ib/bin/activate
#./darknet detector train  /cluster/home/it_stu82/darknet/yolo/darknet.data  /cluster/home/it_stu82/darknet/yolo/darknet-yolov3.cfg ./darknet53.conv.74 -gpus 0,1
#python null.py

python train.py --config=yolact_base_config
