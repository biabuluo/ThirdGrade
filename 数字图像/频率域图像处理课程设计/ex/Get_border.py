# -*-coding:utf-8 -*-
import cv2
import numpy as np

"""
# File       : Get_border
# Time       ：2023/6/14 20:45
# Author     ：chenyu
# version    ：python 3.8
# Description：傅里叶变换+高斯高通滤波器求轮廓/ 轮廓检测
"""
def GaussianHighFrequencyFilter(imarr, sigma=1):
    height, width = imarr.shape
    # print(height, width)
    # 傅里叶变换
    fft = np.fft.fft2(imarr)
    # 居中操作：将低频分量转移到中间
    fft = np.fft.fftshift(fft)

    # 高斯高通滤波函数
    for i in range(height):
        for j in range(width):
            # print(i, j)
            fft[i, j] *= (1 - np.exp(-((i - (height - 1) / 2) ** 2 + (j - (width - 1) / 2) ** 2) / 2 / sigma ** 2))

    # 逆变换
    fft = np.fft.ifftshift(fft)
    ifft = np.fft.ifft2(fft)

    # 取实部
    ifft = np.real(ifft)

    # 获取结果图像
    res = np.zeros((height, width), dtype="uint8")
    max = np.max(ifft)
    min = np.min(ifft)
    # min-max标准化
    for i in range(height):
        for j in range(width):
            res[i, j] = 255 * (ifft[i, j] - min) / (max - min)
    return res



