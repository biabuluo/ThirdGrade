# -*-coding:utf-8 -*-
import numpy as np

from ex import ShowImage, Image2arr

"""
# File       : Medium_ad
# Time       ：2023/6/13 21:57
# Author     ：chenyu
# version    ：python 3.8
# Description：自适应中值滤波器实现
"""
def win_9(win):
    # 判断是否为可疑噪声
    len = win.shape[0]
    temp = int(len//2)
    center = temp
    if win[center, center] == np.max(win) or \
        win[center, center] == np.min(win):
        # 为可疑噪声点
        # 十字方向：四个窗口
        w1 = win[center-temp:center+1, center]
        w2 = win[center:center+temp+1, center]
        w3 = win[center, center-temp:center+1]
        w4 = win[center, center:center+temp+1]
        # X方向：四个窗口
        w5 = []
        for i in range(temp+1):
            w5.append(win[center-i, center-i])
        w5 = np.array(w5)
        w6 = []
        for i in range(temp+1):
            w6.append(win[center-i, center+i])
        w6 = np.array(w6)
        w7 = []
        for i in range(temp+1):
            w7.append(win[center+i, center-i])
        w7 = np.array(w7)
        w8 = []
        for i in range(temp+1):
            w8.append(win[center+i, center+i])
        w8 = np.array(w8)
        # 最后一个窗口：整个模板
        w9 = win
        # 计算中值入表
        medi = [np.median(w1), np.median(w2), np.median(w3), np.median(w4), np.median(w5), np.median(w6), np.median(w7), np.median(w7), np.median(w8)]
        msd = [np.var(w1), np.var(w2), np.var(w3), np.var(w4), np.var(w5), np.var(w6), np.var(w7), np.var(w8), np.var(w9) ]
        # 选择均方差最小的中值返回
        min_index = msd.index(min(msd))
        return medi[min_index]
    else:
        # 信号点
        return win[center, center]




def mediumfilter_9win(img_arr, template_size):
    # 九窗口自适应中值滤波器：
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
    # 0填充完毕
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = win_9(img_arr_filled[i:i+template_size, j:j+template_size])
    # 返回结果
    return result.astype(np.uint8)

if __name__ == '__main__':
    # 对噪声图像进行处理
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper1')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 5)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_9w/c+saltpeper1+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper3')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 5)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_9w/c+saltpeper3+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper5')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 5)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_9w/c+saltpeper5+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+gaussian')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 5)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_9w/c+gaussian+medi.bmp")