# -*-coding:utf-8 -*-
import numpy as np
from utils import *
from ImgArrSwitch import *
"""
# File       : ImgSplitter
# Time       ：2023/6/14 15:57
# Author     ：chenyu
# version    ：python 3.8
# Description：切割图象获取ROI（region of interesting）， 比如把菌落的培养皿以外部分像素点置零
"""



def splitter(img_arr, ratio):
    """
    :param img_arr: 输入图像arr
    :param ratio: 切割比率：最短边的一半的占比
    :return: 返回圆以外的点像素为指定值 区域内平均像素值
    """
    sum, count = 0, 0   # 记录ROI里的像素值总和，计数
    img_arr_cp = np.zeros((img_arr.shape[0], img_arr.shape[1])) #获取副本
    # 计算中间元素坐标
    center_x = int(img_arr.shape[0]//2)
    center_y = int(img_arr.shape[1]//2)
    # 计算半径
    radius = int(ratio*(min(img_arr.shape[0], img_arr.shape[1])/2))
    # 遍历求ROI均值
    for i in range(img_arr_cp.shape[0]):
        for j in range(img_arr_cp.shape[1]):
            if abs(center_x - i)**2 + abs(center_y - j)**2 < int(radius**2):
                sum += img_arr[i, j]
                count += 1
                img_arr_cp[i, j] = img_arr[i, j]
            else: img_arr_cp[i, j] = 0
    val = int(sum / count)
    # 将均值填充到边缘
    for i in range(img_arr_cp.shape[0]):
        for j in range(img_arr_cp.shape[1]):
            if abs(center_x - i)**2 + abs(center_y - j)**2 < int(radius**2):
                sum += img_arr[i, j]
                count += 1
                img_arr_cp[i, j] = img_arr[i, j]
            else: img_arr_cp[i, j] = val
    return img_arr_cp, val

if __name__ == '__main__':
    img = get_img('./img_gray/Colony3.bmp')
    img_arr = image2arr(img)
    print(img_arr.shape[0], img_arr.shape[1])
    img_arr, _ = splitter(img_arr, 0.9)
    print(_)
    img = arr2image(img_arr)
    img.show()


