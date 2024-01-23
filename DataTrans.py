import torch
import numpy as np



class Numpy2Tensor(object):
    def __call__(self, data):
        return torch.Tensor(data)