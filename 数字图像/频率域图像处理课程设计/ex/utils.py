# -*-coding:utf-8 -*-
import PIL.Image
import numpy as np
from scipy import ndimage as ndi
from matplotlib import  pyplot as plt
"""
# File       : utils
# Time       ：2023/6/14 16:33
# Author     ：chenyu
# version    ：python 3.8
# Description：实现一些功能
"""
class Counter:
    def getimg_arr(self, img_arr):
        self._img_arr = img_arr

    def count(self):
        """
        对图像的菌落数计数（深度优先搜索）
        :param img_arr: 图像
        :return: 数量
        """
        l, w = self._img_arr.shape
        count = 0  # 计数器
        for i in range(l):
            for j in range(w):
                if self._img_arr[i][j] == 255:
                    self.dfs_f(i, j, l, w)
                    count += 1
        return count

    def dfs_f(self, i, j, l, w):
        """
        深度优先搜索
        :param img_arr: 二维数组
        :param i:
        :param j:
        :return: 二维数组
        """
        if not (0 <= i < l and 0 <= j < w):
            return
        if self._img_arr[i][j] != 255:
            return
        # 设置为1，避免重复遍历
        self._img_arr[i][j] = 1
        self.dfs_f(i - 1, j, l, w)
        self.dfs_f(i + 1, j, l, w)
        self.dfs_f(i, j - 1, l, w)
        self.dfs_f(i, j + 1, l, w)



def fillfunc(img: np.ndarray):
    """
    填充函数——孔动填充
    :param img: 二值图像
    :return: 填充二值图像
    """
    res = ndi.binary_fill_holes(img)
    res = res.astype(np.uint16)
    res[np.where(res == 1)] = 255
    return res

def get_img(path):
    """
    获取图像
    :param path: 路径
    :return: 图像
    """
    image = PIL.Image.open(path)
    return image

def switch(img_arr):
    """
    :param img_arr:图像
    :return:  二值互换
    """
    return np.where(img_arr==0, 255, 0)

def show_multi_images(row, column, images, imageNames, scale):
    # row, column->整个图的子图排列
    # images->图像list
    # imageNames->图像名称集合
    # scale->子图的大小
    # 函数作用：用subplt显示多张图片的母图
    package = zip(images, imageNames)
    plt.figure("compare", figsize=(scale, scale))
    c = 1
    for i in package:
        plt.subplot(row, column, c)
        temp = list(i)
        plt.imshow(temp[0], cmap="gray")
        plt.title(temp[1])
        plt.axis('off')  # 不显示坐标轴
        c = c+1
    plt.tight_layout()
    plt.show()

def get_imags(paths, imageNamelist):
    # imageNamelist->图像名称list
    # 函数作用：获取图像image列表
    imagelist = []
    for i in zip(paths, imageNamelist):
        i = list(i)
        img, imgname = get_image(i[0], i[1])
        imagelist.append(img)
    return imagelist, imageNamelist

def get_image(path, imageName):
    # imageName->图像名称
    # 函数作用：获取图像image
    location = path + imageName + ".bmp"
    image = PIL.Image.open(location)
    return image, imageName