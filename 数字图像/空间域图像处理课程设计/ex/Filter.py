# -*-coding:utf-8 -*-
import PIL
import numpy as np
import Image2arr
from ex import ShowImage

"""
# File       : Filter
# Time       ：2023/6/13 21:00
# Author     ：chenyu
# version    ：python 3.8
# Description：包含各种滤波器实现
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

def bilateralfilter(img_arr, template_size, sigma_g, sigma_s):
    # 双边滤波器：
    #   1.求出高斯核，空间滤波核
    #   2.两核相乘再归一化 kernel = kernel_g * kernel_s    kernel = kernel/sum(kernel)
    # img_arr->待处理图像arr形式
    # template_size -> 模板大小:得是奇数！！！>1
    # sigma->高斯函数的参数-> 越大高斯函数越宽，越平滑->均值模板
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
            kernel_s = np.zeros((template_size, template_size))   # 计算每个坐标点的空间域滤波核
            for k in range(i, i+template_size):
                for l in range(j, j+template_size):
                    kernel_s[k-i][l-j] =np.exp(-0.5*pow((img_arr_filled[k][l]-img_arr[i][j]), 2)/(sigma_s ** 2))
            kernel = kernel_g * kernel_s
            kernel = kernel/np.sum(kernel)
            result[i][j] = np.sum(img_arr_filled[i:i+template_size, j:j+template_size] * kernel)
    # 截断
    np.clip(result, 0, 255)
    # 返回结果
    return result.astype(np.uint8)

def gaussianfilter(img_arr, template_size, sigma):
    # 高斯滤波器：
    #   1.计算每个模板元素的权重+归一化（softmax?）
    #   2.权重模板与图像对应元素相乘
    #   3.求和得中心点元素
    # img_arr->待处理图像arr形式
    # template_size -> 模板大小:得是奇数！！！>1
    # sigma->高斯函数的参数-> 越大高斯函数越宽，越平滑->均值模板
    height, width = img_arr.shape        # 图像长宽
    # 为了方便-> 采用0填充
    lines = template_size // 2           # 一边单侧添加行数
    zero_bottom = np.zeros((height + 2 * lines, width + 2 * lines))
    for i in range(height):
        for j in range(width):
            zero_bottom[i+lines, j+lines] = img_arr[i][j]
    img_arr_filled = zero_bottom
    # 计算卷积核
    kernel = gaussiankernel(template_size, sigma)
    kernel /= kernel.sum()
    # 开始卷积
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = np.sum(kernel * img_arr_filled[i:i+template_size, j:j+template_size])
    # 截断
    np.clip(result, 0, 255)
    # 返回结果
    return result.astype(np.uint8)


def meanfilter(img_arr, template_size):
    # 均值滤波器：使用模板内部像素的平均值做中心点的像素值
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
    # 开始卷积
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = np.mean(img_arr_filled[i:i+template_size, j:j+template_size])
    # 返回结果
    return result.astype(np.uint8)

if __name__ == '__main__':
    # 对c+noise.bmp进行处理
    # img, name = ShowImage.get_img("./img_noise/", 'c+gaussian')
    # img_arr = Image2arr.image2arr(img)
    # img_arr_mean = meanfilter(img_arr, 5)
    # img_arr_medium = mediumfilter(img_arr, 5)
    # img_arr_gaussian = gaussianfilter(img_arr, 5, 0.8)
    # img_arr_bilateral = bilateralfilter(img_arr, 5, 50, 50)
    #
    # # 保存图像
    # img_mean = Image2arr.arr2image(img_arr_mean)
    # img_mean.save("./result/c+gaussian+mean.bmp")
    # img_medium = Image2arr.arr2image(img_arr_medium)
    # img_medium.save("./result/c+gaussian+medi.bmp")
    # img_gaussian = Image2arr.arr2image(img_arr_gaussian)
    # img_gaussian.save("./result/c+gaussian+g.bmp")
    # img_bilateral = Image2arr.arr2image(img_arr_bilateral)
    # img_bilateral.save("./result/c+gaussian+b.bmp")
    #
    # # 对c+noise.bmp进行处理
    # img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper1')
    # img_arr = Image2arr.image2arr(img)
    # img_arr_mean = meanfilter(img_arr, 5)
    # img_arr_medium = mediumfilter(img_arr, 5)
    # img_arr_gaussian = gaussianfilter(img_arr, 5, 0.8)
    # img_arr_bilateral = bilateralfilter(img_arr, 5, 50, 50)
    #
    # # 保存图像
    # img_mean = Image2arr.arr2image(img_arr_mean)
    # img_mean.save("./result/c+saltpeper1+mean.bmp")
    # img_medium = Image2arr.arr2image(img_arr_medium)
    # img_medium.save("./result/c+saltpeper1+medi.bmp")
    # img_gaussian = Image2arr.arr2image(img_arr_gaussian)
    # img_gaussian.save("./result/c+saltpeper1+g.bmp")
    # img_bilateral = Image2arr.arr2image(img_arr_bilateral)
    # img_bilateral.save("./result/c+saltpeper1+b.bmp")

    # # 使用中值滤波器对高密度椒盐噪声处理
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper3')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter(img_arr, 5)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result/c+saltpeper3+medi.bmp")
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper5')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter(img_arr, 5)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result/c+saltpeper5+medi.bmp")