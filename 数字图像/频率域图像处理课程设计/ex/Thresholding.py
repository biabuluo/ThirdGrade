# -*-coding:utf-8 -*-
import numpy as np
from Erode_huge import *
from ex.ImgArrSwitch import image2arr, arr2image
from ex.ImgSplitter import splitter
from ex.utils import get_img

"""
# File       : Thresholding
# Time       ：2023/6/14 16:48
# Author     ：chenyu
# version    ：python 3.8
# Description：对图像进行二值化
"""
# 统计灰度直方图
def sumOfAll(array: np.ndarray) -> np.ndarray:
    # 获得对应灰度值的个数
    result = []
    # 灰度值列表
    for i in range(256):
        # 遍历 256 个灰度值
        result.append(np.sum(array == i))
        # 添加对应的灰度值像素点个数进入灰度值列表中
    return np.array(result)
    # 返回结果，类型为 np 数组


# 根据三角型法找到阈值
def getThreshold(array: np.ndarray)-> int:
    """
    :param array: 图像二维数组
    :return: int类型阈值
    """
    # 获取图像长宽
    # 计算图像的灰度直方图
    hist = sumOfAll(array)
    # 找到最高点和最左边的零点
    max_value = max(hist)
    max_index = np.where(hist == max_value)[0][0]
    left_index = 0
    for i in range(256):
        if hist[i] > 0:
            left_index = i
            break
    right_index = 255
    for i in range(255, -1, -1):
        if hist[i] > 0:
            right_index = i
            break
    # 根据最高点和零点连成一条直线，然后找到直方图上离直线最远的一点，设置该点的灰度值为阈值
    k = b = l = r = T = 0
    # 初始化直线斜率、直线截距、左边界、右边界、阈值
    max_dist = 0
    # 最大距离
    # 根据哪个零点距离最高点最远判断使用哪个零点
    if abs(max_index - left_index) > abs(max_index - right_index):
        k = max_value / (max_index - left_index)
        b = left_index - max_index
        l = left_index + 1
        r = max_index + 1
    else:
        k = -(max_value / (right_index - max_index))
        b = right_index - max_index
        l = max_index + 1
        r = right_index + 1
    # 寻找阈值
    for i in range(l, r):
        dist = k * i + b * hist[i]
        # 计算点到直线之间的距离
        if dist > max_dist:
            max_dist = dist
            T = i
    return T



def thresholding(img_arr, threshold_val):
    """
    :param img_arr: 图像arr
    :param threshold_val:阈值
    :return: 二值图像
    """
    return np.where(img_arr>threshold_val, 255, 0)


if __name__ == '__main__':
    img = get_img('./img_gray/Colony.bmp')
    img_arr = image2arr(img)
    img_arr, avg = splitter(img_arr, 0.9, 255)
    min_pixel = np.min(img_arr)
    img_arr = thresholding(img_arr, min_pixel+80)
    img_arr = closef(img_arr, 3)
    img = arr2image(img_arr)
    img.show()


