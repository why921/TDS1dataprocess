from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms
import DataTrans
import numpy as np
import os


class DDMDataSet(Dataset):
    """自定义数据集"""

    def __init__(self, labeltxt, transform, target_transform=None):
        fh = open(labeltxt, 'r')
        imgs = []
        for line in fh:
            line = line.rstrip()  # 删除 本行string 字符串末尾的指定字符
            words = line.split()  # 通过指定分隔符对字符串进行切片，默认为所有的空字符，包括空格、换行、制表符等
            imgs.append((words[0], int(words[1])))  # 把txt里的内容读入imgs列表保存
            # words[0]图片，words[1]lable
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform


    def __getitem__(self, index):
        fn, label = self.imgs[index]  # fn图片path #fn和label分别获得imgs[index]即每行中word[0]和word[1]的信息
        img=np.load(fn)
        img=img/1.0
        if self.transform is not None:
            img = self.transform(img)
        return img, label


    def __len__(self):
        return len(self.imgs)

data_transforms = transforms.Compose([
   DataTrans.Numpy2Tensor(),
])


ddss = DDMDataSet(labeltxt='E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\pa.txt',transform=data_transforms)
ddss.__init__(labeltxt='E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\pa.txt',transform=data_transforms)
print(ddss.__len__())
img, gt = ddss.__getitem__(2) # get the 34th sample
print(type(img))
print(img)
print(gt)