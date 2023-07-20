# -*-coding:utf-8 -*-
import numpy as np
"""
# File       : Main
# Time       ：2023/6/14 15:06
# Author     ：chenyu
# version    ：python 3.8
# Description：类菌落计数
"""
from ex.Filter import mediumfilter
from ex.Erode_huge import openf, closef, huge_bin_image, erode_bin_image
from ex.ImgArrSwitch import image2arr, arr2image
from ex.ImgSplitter import splitter
from ex.Thresholding import thresholding, getThreshold
from ex.utils import get_img, switch, fillfunc, show_multi_images, get_imags
from ex.utils import Counter
from Get_border import GaussianHighFrequencyFilter

def colony(name):
    """
    对菌落图像进行边缘识别等一系列操作
    :param name:colony图像名称
    :return:存储结果图像
    """
    path = './img_gray/'+name+'.bmp'
    # 对colony操作
    img = get_img(path)
    # 获取图像转为数组
    img_arr = image2arr(img)
    # 简单的切割图像
    img_arr, _ = splitter(img_arr, 0.90)
    # 中值滤波处理图像
    img_arr = mediumfilter(img_arr, 3)
    img_arr = GaussianHighFrequencyFilter(img_arr, 10)
    # 保存边缘图像
    img = arr2image(img_arr)
    img.save('./img_afterprocessed/'+name+'_edge.bmp')
    # 二值化
    threshold_val = getThreshold(img_arr)
    img_arr = thresholding(img_arr, threshold_val)
    # 二值转换一下(白->黑 黑->白)
    img_arr = switch(img_arr)
    # 开运算
    img_arr = openf(img_arr, 3)
    img = arr2image(img_arr)
    # img.show()
    # 结果图像保存
    img.save('./img_afterprocessed/'+name+'_res.bmp')

def coins(name):
    """
    对硬币图像进行边缘识别等一系列操作
    :param name:colony图像名称
    :return:存储结果图像
    """
    path = './img_gray/'+name+'.bmp'
    img = get_img(path)
    # 获取图像转为数组
    img_arr = image2arr(img)
    # 边缘检测
    img_arr = GaussianHighFrequencyFilter(img_arr, 10)
    img = arr2image(img_arr)
    img.save('./img_afterprocessed/'+name+'_edge.bmp')
    # 二值化
    threshold_val = getThreshold(img_arr)
    img_arr = thresholding(img_arr, threshold_val)
    # img = arr2image(img_arr)   # test
    # img.show()
    #  填充
    img_arr = fillfunc(img_arr)
    # 开函数
    img_arr = openf(img_arr, 5)
    img = arr2image(img_arr)
    # img.show()
    # 结果图像保存
    img.save('./img_afterprocessed/'+name+'_res.bmp')

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)  # 设置递归深度限制
    # colony操作
    # colony('Colony1')
    # colony('Colony2')
    # colony('Colony3')


    # coins操作
    # coins('coins1')
    # coins('coins2')


    # 对colony计数操作
    # 定义一个计数器
    mycounter = Counter()
    img1 = get_img('./img_afterprocessed/Colony1_res.bmp')
    img2 = get_img('./img_afterprocessed/Colony2_res.bmp')
    img3 = get_img('./img_afterprocessed/Colony3_res.bmp')
    # 获取图像转为数组
    img_arr1 = image2arr(img1)
    img_arr2 = image2arr(img2)
    img_arr3 = image2arr(img3)
    mycounter.getimg_arr(img_arr1)
    print('Colony1计数：', mycounter.count())
    mycounter.getimg_arr(img_arr2)
    print('Colony2计数：', mycounter.count())
    mycounter.getimg_arr(img_arr3)
    print('Colony3计数：', mycounter.count())

    # 对coins计数操作
    # 定义一个计数器
    mycounter = Counter()
    img1 = get_img('./img_afterprocessed/coins1_res.bmp')
    img2 = get_img('./img_afterprocessed/coins2_res.bmp')
    # 获取图像转为数组
    img_arr1 = image2arr(img1)
    img_arr2 = image2arr(img2)
    mycounter.getimg_arr(img_arr1)
    print('coins1计数：', mycounter.count())
    mycounter.getimg_arr(img_arr2)
    print('coins2计数：', mycounter.count())

    # 展示colony图像处理结果
    imageNamelist = ["Colony1",
                     "Colony1_edge",
                     "Colony1_res",
                     "Colony2",
                     "Colony2_edge",
                     "Colony2_res",
                     "Colony3",
                     "Colony3_edge",
                     "Colony3_res" ]
    imagePaths = ["./img_gray/",
                  "./img_afterprocessed/",
                  "./img_afterprocessed/",
                  "./img_gray/",
                  "./img_afterprocessed/",
                  "./img_afterprocessed/",
                  "./img_gray/",
                  "./img_afterprocessed/",
                  "./img_afterprocessed/"]
    show_multi_images(3, 3, get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )

    # 展示coins图片处理结果
    imageNamelist = ["coins1",
                     "coins1_edge",
                     "coins1_res",
                     "coins2",
                     "coins2_edge",
                     "coins2_res"]
    imagePaths = ["./img_gray/",
                  "./img_afterprocessed/",
                  "./img_afterprocessed/",
                  "./img_gray/",
                  "./img_afterprocessed/",
                  "./img_afterprocessed/"]
    show_multi_images(2, 3, get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )


