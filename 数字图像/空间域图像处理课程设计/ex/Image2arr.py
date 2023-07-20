# -*-coding:utf-8 -*-
import numpy as np
import ShowImage
from PIL import Image
"""
# File       : Image2arr
# Time       ：2023/6/13 21:05
# Author     ：chenyu
# version    ：python 3.8
# Description：图像与arr互相转换
"""
def image2arr(img):
    return np.array(img)

def arr2image(arr):
    return Image.fromarray(arr).convert('L')