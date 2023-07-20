# -*-coding:utf-8 -*-
import numpy as np

from ex import ShowImage, Image2arr

"""
# File       : result_9w_ad
# Time       ：2023/6/15 23:39
# Author     ：chenyu
# version    ：python 3.8
# Description：
"""
def win_9(Gmax, Gmin, max_win, i, j, img_arr, T1):
    template_size = 3
    h, w = img_arr.shape  # 图像长宽
    while True:
        temp = int(template_size//2)
        center = temp
        # win 当前窗口
        win = np.zeros((template_size, template_size))
        for k in range(i - temp, i + temp + 1):
            for l in range(j - temp, j + temp + 1):
                # 判断是否出界
                if k < 0 or k >= h or l < 0 or l >= w:
                    continue
                else:
                    win[center - (i - k), center - (j - l)] = img_arr[k, l]
        # 全局判断
        if np.abs(img_arr[i, j]-Gmin) > T1 and \
            np.abs(img_arr[i, j]-Gmax) > T1:
            # 信号点
            return win[center, center]
        else:
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
            # 判断最小均方差中值是否仍为可疑噪声
            if medi[min_index]>Gmin and medi[min_index]<Gmax:
                return medi[min_index]
            else:
                template_size += 2
                if template_size < max_win:
                    continue
                else:
                    return medi[min_index]


def mediumfilter_9win(img_arr, max_size,  T1):
    # 九窗口自适应中值滤波器：
    # 将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值
    # img_arr->待处理图像arr形式
    # template_size -> 模板大小:得是奇数！！！>1
    height, width = img_arr.shape        # 图像长宽
    Gmax = np.max(img_arr)
    Gmin = np.min(img_arr)
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = win_9(Gmax, Gmin, max_size, i, j, img_arr, T1)
    # 返回结果
    return result.astype(np.uint8)

if __name__ == '__main__':
    # 对噪声图像进行处理
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper1')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 9, 10)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.show()
    img_medium.save("./result_9w_ad/c+saltpeper1+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper3')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 9, 10)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.show()
    img_medium.save("./result_9w_ad/c+saltpeper3+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper5')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 9, 10)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.show()
    img_medium.save("./result_9w_ad/c+saltpeper5+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+gaussian')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_9win(img_arr, 9, 10)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.show()
    img_medium.save("./result_9w_ad/c+gaussian+medi.bmp")