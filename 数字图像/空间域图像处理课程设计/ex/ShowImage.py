# -*-coding:utf-8 -*-
from matplotlib import pyplot as plt
import PIL.Image
"""
# File       : ShowImage
# Time       ：2023/6/13 21:04
# Author     ：chenyu
# version    ：python 3.8
# Description：获取图片+展示图片
"""
def get_imags(paths, imageNamelist):
    # imageNamelist->图像名称list
    # 函数作用：获取图像image列表
    imagelist = []
    for i in zip(paths, imageNamelist):
        i = list(i)
        img, imgname = get_img(i[0], i[1])
        imagelist.append(img)
    return imagelist, imageNamelist

def get_img(path, imageName):
    # imageName->图像名称
    # 函数作用：获取图像image
    location = path + imageName + ".bmp"
    image = PIL.Image.open(location)
    return image, imageName

def show_single_image(image, imageName):
    # image->图像
    # imageName->图像名称
    # 函数作用：用plt显示单张图片
    plt.figure("single_figure")
    plt.imshow(image, cmap="gray")
    plt.axis('off')  # 不显示坐标轴
    plt.title(imageName)
    plt.show()

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

if __name__ == '__main__':
    # 以下为测试代码
    # image, imageName = get_img("Cameraman")
    # show_single_image(image, imageName)
    imageNamelist = []
    imageNamelist.append("Cameraman")
    imageNamelist.append("Goldhill")
    imageNamelist.append("lena")
    paths = ["./images/", "./images/", "./images/"]
    #
    show_multi_images(1, 3, get_imags(paths, imageNamelist)[0], imageNamelist, 10)
    # print(list(zip(imagelist, imageNamelist, description)))
    # print(get_imags(imageNamelist))