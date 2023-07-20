# -*-coding:utf-8 -*-
from PIL import Image
"""
# File       : RGB2gray
# Time       ：2023/6/14 15:39
# Author     ：chenyu
# version    ：python 3.8
# Description：RGB图像转为灰度图
"""

def rgb2gray(name, savename):
    """
    :param name: 图像名称
    :param savename: 保存名称
    :return:
    """
    input_path = './img/'+name
    output_path = './img_gray/'+savename
    I = Image.open(input_path)
    # I.show()
    L = I.convert('L')
    L.show()
    L.save(output_path)

if __name__ == '__main__':
    rgb2gray('Colony1.bmp', 'Colony1.bmp')
    rgb2gray('Colony2.png', 'Colony2.bmp')
    rgb2gray('Colony3.jpg', 'Colony3.bmp')
    rgb2gray('coins1.png', 'coins1.bmp')
    rgb2gray('coins2.png', 'coins2.bmp')
