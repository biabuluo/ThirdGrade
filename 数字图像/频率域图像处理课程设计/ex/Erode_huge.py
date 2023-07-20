# -*-coding:utf-8 -*-
import numpy as np
"""
# File       : Erode_huge
# Time       ：2023/6/14 17:27
# Author     ：chenyu
# version    ：python 3.8
# Description：实现腐蚀、膨胀操作/ 开运算、闭运算
"""

def openf(img_arr, size): # 开运算
    # 先蚀刻再膨胀
    img_arr = erode_bin_image(img_arr, size)
    img_arr = huge_bin_image(img_arr, size)
    return img_arr

def closef(img_arr, size): # 闭运算
    # 先膨胀再蚀刻
    img_arr = huge_bin_image(img_arr, size)
    img_arr = erode_bin_image(img_arr, size)
    return img_arr



def huge_bin_image(bin_image, size):
    kernel = np.ones(shape=(size, size))
    """
    膨胀
    Args:二维数组，模板大小
    Returns: 图像二维数组
    """
    kernel_size = kernel.shape[0]
    d_image = np.zeros(shape=bin_image.shape)
    center_move = int((kernel_size-1)/2)
    for i in range(center_move, bin_image.shape[0]-kernel_size+1):
        for j in range(center_move, bin_image.shape[1]-kernel_size+1):
            d_image[i, j] = np.max(bin_image[i-center_move:i+center_move, j-center_move:j+center_move])
    return d_image

def erode_bin_image(bin_image, size):
    kernel = np.ones(shape=(size, size))
    """
    蚀刻
    Args:图像二维数组，模板大小
    Returns: 图像二维数组
    """
    kernel_size = kernel.shape[0]
    d_image = np.zeros(shape=bin_image.shape)
    center_move = int((kernel_size-1)/2)
    for i in range(center_move, bin_image.shape[0]-kernel_size+1):
        for j in range(center_move, bin_image.shape[1]-kernel_size+1):
            d_image[i, j] = np.min(bin_image[i-center_move:i+center_move, j-center_move:j+center_move])
    return d_image
