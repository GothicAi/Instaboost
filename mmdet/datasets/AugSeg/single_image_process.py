# coding:utf-8

import math
import random
import numpy as np
from .config import AugSegConfig


def get_transform(src: np.ndarray, restricts: dict, config: AugSegConfig):
    action_candidate = config.action_candidate
    action_prob = config.action_prob

    if 'noflip' in restricts and restricts['noflip'] == 1:
        if 'horizontal' in action_candidate or 'vertical' in action_candidate:
            flip_idx = np.where((action_candidate == 'horizontal') + (action_candidate == 'vertical'))[0]
            action_candidate = np.delete(action_candidate, flip_idx)
            action_prob = np.delete(action_prob, flip_idx)
            action_prob = action_prob / np.sum(action_prob)
        assert 'horizontal' not in action_candidate and 'vertical' not in action_candidate
        assert np.sum(action_prob) == 1
        assert len(action_candidate) == len(action_prob)

    action_what = np.random.choice(action_candidate, p=action_prob)

    if action_what == 'skip':
        t = __identity_transform()
    elif action_what == 'horizontal':
        src = src[:, ::-1, :]  # horizontal flip
        t = __random_transform(restricts, config)
        t['flip'] = 'horizontal'
    elif action_what == 'vertical':
        src = src[::-1, :, :]  # vertical flip
        t = __random_transform(restricts, config)
        t['flip'] = 'vertical'
    elif action_what == 'normal':
        t = __random_transform(restricts, config)
    else:
        raise ValueError('Unknown action {}'.format(action_what))

    return src, t


def __random_transform(restricts: dict, config: AugSegConfig):
    t = dict()
    t['s'] = random.uniform(*config.scale)
    max_x = restricts['bbox_w'] // config.dx
    t['tx'] = random.randint(-max_x, max_x)
    max_y = restricts['bbox_h'] // config.dy
    t['ty'] = random.randint(-max_y, max_y)
    t['theta'] = math.radians(random.randint(*config.theta))

    if 'restrict_left' in restricts and restricts['restrict_left'] == 1:
        t['s'] = max(t['s'], 1)
        t['tx'] = min(t['tx'], 0)
        t['theta'] = 0
    if 'restrict_right' in restricts and restricts['restrict_right'] == 1:
        t['s'] = max(t['s'], 1)
        t['tx'] = max(t['tx'], 0)
        t['theta'] = 0
    if 'restrict_up' in restricts and restricts['restrict_up'] == 1:
        t['s'] = max(t['s'], 1)
        t['ty'] = min(t['ty'], 0)
        t['theta'] = 0
    if 'restrict_down' in restricts and restricts['restrict_down'] == 1:
        t['s'] = max(t['s'], 1)
        t['ty'] = max(t['ty'], 0)
        t['theta'] = 0

    return t


def __identity_transform():
    t = dict()
    t['s'] = 1
    t['tx'] = 0
    t['ty'] = 0
    t['theta'] = 0
    return t


def get_restriction(bndbox, width, height):
    """
    Restrict transform parameters.
    :param bndbox: bounding box of original object in [xmin, ymin, xmax, ymax]
    :param width: image width
    :param height: image height
    :return: a dictionary containing restrictions
    """
    xmin, ymin, xmax, ymax = bndbox
    restricts = dict()
    restricts['bbox_w'] = xmax - xmin
    restricts['bbox_h'] = ymax - ymin
    if xmin < 10:
        restricts['restrict_left'] = 1
        restricts['noflip'] = 1
    if xmax > width - 10:
        restricts['restrict_right'] = 1
        restricts['noflip'] = 1
    if ymin < 10:
        restricts['restrict_up'] = 1
        restricts['noflip'] = 1
    if ymax > height - 10:
        restricts['restrict_down'] = 1
        restricts['noflip'] = 1
    return restricts
