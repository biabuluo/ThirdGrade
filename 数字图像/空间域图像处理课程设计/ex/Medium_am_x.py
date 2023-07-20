# -*-coding:utf-8 -*-
from ex import ShowImage, Image2arr
import numpy as np
"""
# File       : Medium_am_x
# Time       ：2023/6/14 11:06
# Author     ：chenyu
# version    ：python 3.8
# Description：x型自适应中值滤波器
"""

def judge(max_win, i, j, img_arr, h, w):
    template_size = 3
    # 判定函数
    while True:
        temp = int(template_size//2)
        center = temp
        # base 当前窗口
        base = np.zeros((template_size, template_size))
        for k in range(i - temp, i + temp + 1):
            for l in range(j - temp, j + temp + 1):
                # 判断是否出界
                if k < 0 or k >= h or l < 0 or l >= w:
                    continue
                else:
                    base[center - (i - k), center - (j - l)] = img_arr[k, l]
        # 获取对角元素
        ele = list(np.diagonal(base))
        # 反对角
        ele = ele + list(np.diag(np.fliplr(base)))
        ele.remove(base[center, center])  # 去掉一个重复的中心元素
        Gmin = np.max(base)
        Gmax = np.min(base)
        if img_arr[i, j]-Gmin > 0 and \
            img_arr[i, j]-Gmax < 0:
            b1 = img_arr[i, j] - Gmin
            b2 = img_arr[i, j] - Gmax
            if b1 > 0 and b2 < 0:
                return img_arr[i, j]
            else: return np.median(ele)
        else:
            template_size += 2
            if template_size < max_win:
                continue
            else: return np.median(ele)


def mediumfilter_am_x(img_arr, max_win):
    # 中值滤波器：
    # 将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值
    # img_arr->待处理图像arr形式
    # max_win -> 最大模板大小:得是奇数！！！>1
    height, width = img_arr.shape        # 图像长宽
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = judge(max_win, i, j, img_arr, height, width)
    # 返回结果
    return result.astype(np.uint8)

if __name__ == '__main__':
    # 对噪声图像进行处理
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper1')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_am_x(img_arr, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_x/c+saltpeper1+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper3')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_am_x(img_arr, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_x/c+saltpeper3+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper5')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_am_x(img_arr, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_x/c+saltpeper5+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+gaussian')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_am_x(img_arr, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_x/c+gaussian+medi.bmp")
