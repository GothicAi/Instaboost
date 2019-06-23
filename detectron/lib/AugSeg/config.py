import numpy as np


class AugSegConfig:
    def __init__(self, action_candidate: tuple = ('normal', 'horizontal', 'skip'),
                 action_prob: tuple = (1, 0, 0), scale: tuple = (0.8, 1.2), dx: float = 15, dy: float = 15,
                 theta=(-1, 1), color_prob=0.5, heatmap_flag=False):
        """
        :param action_candidate: tuple of action candidates. 'normal', 'horizontal', 'vertical', 'skip' are supported
        :param action_prob: tuple of corresponding action probabilities. Should be the same length as action_candidate
        :param scale: tuple of (min scale, max scale)
        :param dx: the maximum x-axis shift will be  (instance width) / dx
        :param dy: the maximum y-axis shift will be  (instance height) / dy
        :param theta: tuple of (min rotation degree, max rotation degree)
        :param color_prob: the probability of images for color augmentation
        :param heatmap_flag: whether to use heatmap guided
        """
        assert len(action_candidate) == len(action_prob), 'Candidate & probability length mismatch'
        assert np.sum(action_prob) == 1, 'Probability must sum to 1'
        assert len(scale) == 2, 'scale should have 2 items (min scale, max scale)'
        assert len(theta) == 2, 'theta should have 2 items (min theta, max theta)'

        self.action_candidate = np.array(action_candidate)
        self.action_prob = np.array(action_prob)
        self.scale = scale
        self.dx = dx
        self.dy = dy
        self.theta = theta
        self.color_prob = color_prob
        self.heatmap_flag = heatmap_flag
