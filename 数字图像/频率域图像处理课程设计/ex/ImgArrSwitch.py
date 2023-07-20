# -*-coding:utf-8 -*-
import numpy as np
from PIL import Image
"""
# File       : ImgArrSwitch
# Time       ：2023/6/14 15:55
# Author     ：chenyu
# version    ：python 3.8
# Description：图像和arr互相转换
"""
def image2arr(img):
    return np.array(img)

def arr2image(arr):
    return Image.fromarray(arr).convert('L')