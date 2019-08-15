# InstaBoost

A python implementation for paper: "**InstaBoost: Boosting Instance Segmentation Via Probability Map Guided Copy-Pasting**". The code has been released on PyPI for easier installation and implementation. 

## Install

```
pip install InstaBoost
```

Only tested on python3 and Linux. Windows is not supported since pycocotools do not support Windows. 

## Get Started

There are two main interface in **InstaBoost**.

### **InstaBoostConfig**

```
cfg = InstaBoostConfig(action_candidate: tuple,
                       action_prob: tuple, 
                       scale: tuple, 
                       dx: float, 
                       dy: float,
                       theta: tuple, 
                       color_prob: float, 
                       heatmap_flag: bool)
```
Parameters: 

**action_candidate:** tuple of action candidates. 'normal', 'horizontal', 'vertical', 'skip' are supported

**action_prob:** tuple of corresponding action probabilities. Should be the same length as action_candidate

**scale:** tuple of (min scale, max scale)

**dx:** the maximum x-axis shift will be  (instance width) / dx

**dy:** the maximum y-axis shift will be  (instance height) / dy

**theta:** tuple of (min rotation degree, max rotation degree)

**color_prob:** the probability of images for color augmentation

**heatmap_flag:** whether to use heatmap guided

Output:

**cfg:** a InstaBoostConfig instance

### **get_new_data**

```
new_ann, new_img = get_new_data(ori_anns: list, 
                                ori_img: np.ndarray, 
                                config: InstaBoostConfig, 
                                background: np.ndarray)
```
Parameters: 

**ori_anns:** list of coco-style annotation dicts

**ori_img:** image corresponding to ori_anns

**config:** a InstaBoostConfig instance. If None, the default parameters will be used

**background:** if not None, this background image will be used for augmentation

Output:

**new_ann:** ori_anns after augmentation without changes in length of list or keys of dicts

**new_img:** ori_img after augmentation without changes in shape

## Samples and models

We show how to implement our method on two main segmentation frameworks: [Detectron](https://github.com/roytseng-tw/Detectron.pytorch) and [mmdetection](https://github.com/open-mmlab/mmdetection) in repo [InstaBoost-sample](https://github.com/GothicAi/Instaboost). Results and models trained with InstaBoost are available in the [Model zoo](MODEL_ZOO.md).
