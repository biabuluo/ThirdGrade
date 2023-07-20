# -*-coding:utf-8 -*-
import numpy as np
"""
# File       : Filter
# Time       ：2023/6/14 16:04
# Author     ：chenyu
# version    ：python 3.8
# Description：中值滤波处理图像
"""
def mediumfilter(img_arr, template_size):
    # 中值滤波器：
    # 将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值
    # img_arr->待处理图像arr形式
    # template_size -> 模板大小:得是奇数！！！>1
    height, width = img_arr.shape        # 图像长宽
    # 为了方便-> 采用0填充
    lines = template_size // 2           # 一边单侧添加行数
    zero_bottom = np.zeros((height + 2 * lines, width + 2 * lines))
    for i in range(height):
        for j in range(width):
            zero_bottom[i+lines, j+lines] = img_arr[i][j]
    img_arr_filled = zero_bottom
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = np.median(img_arr_filled[i:i+template_size, j:j+template_size])
    # 返回结果
    return result.astype(np.uint8)