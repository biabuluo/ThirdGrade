# -*-coding:utf-8 -*-
import numpy as np
import ShowImage
from ex import Image2arr

"""
# File       : Medium_bil
# Time       ：2023/6/14 11:18
# Author     ：chenyu
# version    ：python 3.8
# Description：双边滤波与中值滤波自适应算法
"""

def replace(img_arr, i, j, max_win, h, w):
    template_size = 3  # 初始模板大小
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
        # 判断窗口内是否有噪点
        pixel = []
        for k in range(base.shape[0]):
            for l in range(base.shape[1]):
                if base[k, l] != 0 and base[k, l] !=255:
                    pixel.append(base[k, l])
        if len(pixel) != 0 :
            return np.median(pixel)
        else:
            template_size += 2 # 中值滤波模板自适应增大
            if template_size > max_win:
                return seek(img_arr, i, j)
            else: continue


def seek(img_arr, i, j):   # 寻找该点上一个非噪点的像素值返回
    result = np.median(img_arr)    # 都没有只能返回整张图片的中值
    for k in range(0, i+1, -1):
        flag = False
        for l in range(0, j+1, -1):
            if img_arr[k, l] != 0 and img_arr[k, l] != 255:
                result = img_arr[k, l]
                flag = True   # 找到了
                break
        if flag: break
    return result




def gaussiankernel(template_size, sigma):
    # 计算高斯核
    # template_size:模板大小
    # sigma:高斯函数参数
    lines = template_size // 2
    kernel = np.zeros((template_size, template_size))
    for i in range(-lines, -lines+template_size):
        for j in range(-lines, -lines+template_size):
            kernel[j+lines, i+lines] = np.exp(-(i ** 2 + j ** 2) / (2 * (sigma ** 2)))
    kernel /= (2 * np.pi * sigma * sigma)       # 注意没有归一化
    return kernel

def bilateralfilter_advanced(img_arr, template_size, sigma_g, sigma_s, max_win):
    # 双边滤波器：
    #   1.求出高斯核，空间滤波核
    #   2.两核相乘再归一化 kernel = kernel_g * kernel_s    kernel = kernel/sum(kernel)
    # img_arr->待处理图像arr形式
    # template_size -> 双边滤波模板大小:得是奇数！！！>1
    # sigma->高斯函数的参数-> 越大高斯函数越宽，越平滑->均值模板
    # max_win-> 中值滤波自适应窗口最大大小
    height, width = img_arr.shape        # 图像长宽
    # 为了方便-> 采用0填充
    lines = template_size // 2           # 一边单侧添加行数
    zero_bottom = np.zeros((height + 2 * lines, width + 2 * lines))
    for i in range(height):
        for j in range(width):
            zero_bottom[i+lines, j+lines] = img_arr[i][j]
    img_arr_filled = zero_bottom
    # 计算高斯核
    kernel_g = gaussiankernel(template_size, sigma_g)
    # 计算值域滤波核并开始卷积
    kernel = np.zeros((template_size, template_size))
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            if img_arr[i][j]==0 or img_arr[i][j]==255:           # 改进
                img_arr[i][j] = replace(img_arr, i, j, max_win, height, width)
            kernel_s = np.zeros((template_size, template_size))   # 计算每个坐标点的值域滤波核
            for k in range(i, i+template_size):
                for l in range(j, j+template_size):
                    if img_arr_filled[k][l] == 0:             # 消除0填充带来的影响
                        img_arr_filled[k][l] = img_arr[i][j]
                    kernel_s[k-i][l-j] =np.exp(-0.5*pow((img_arr_filled[k][l]-img_arr[i][j]), 2)/(sigma_s ** 2))
            kernel = kernel_g * kernel_s
            kernel = kernel/np.sum(kernel)
            result[i][j] = np.sum(img_arr_filled[i:i+template_size, j:j+template_size] * kernel)
    # 截断
    np.clip(result, 0, 255)
    # 返回结果
    return result.astype(np.uint8)

if __name__ == '__main__':
    # 对噪声图像进行处理
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper1')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = bilateralfilter_advanced(img_arr, 5, 50, 50, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_bil/c+saltpeper1+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper3')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = bilateralfilter_advanced(img_arr, 5, 50, 50, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_bil/c+saltpeper3+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper5')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = bilateralfilter_advanced(img_arr, 5, 50, 50, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_bil/c+saltpeper5+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+gaussian')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = bilateralfilter_advanced(img_arr, 5, 50, 50, 9)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_bil/c+gaussian+medi.bmp")