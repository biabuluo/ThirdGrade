# -*-coding:utf-8 -*-
import numpy as np

from ex import ShowImage, Image2arr

"""
# File       : Medium_basenoise
# Time       ：2023/6/13 23:47
# Author     ：chenyu
# version    ：python 3.8
# Description：基于噪点检测自适应中值滤波器
"""

def judge(Gmax, Gmin, max_win, i, j, img_arr, T1, T2, h, w):
    template_size = 3
    # 判定函数
    while True:
        temp = int(template_size//2)
        center = temp
        if np.abs(img_arr[i, j]-Gmin) > T1 and \
            np.abs(img_arr[i, j]-Gmax) > T1:
            # 非噪声点
            return img_arr[i, j]
        else:
            base = np.zeros((template_size, template_size))
            for k in range(i-temp, i+temp+1):
                for l in range(j-temp, j+temp+1):
                    # 判断是否出界
                    if k<0 or k>=h or l<0 or l>=w:
                        continue
                    else: base[center-(i-k), center-(j-l)] = img_arr[k, l]
            SM = np.median(base) # 获取窗口的标准中值
            if SM>Gmin and SM<Gmax:
                # 5
                sum = 0
                for k in range(template_size):
                    for l in range(template_size):
                        if k==center and l==center:
                            continue
                        else: sum+=np.abs(base[center, center] - base[k, l])
                avg = sum/(template_size**2-1)
                if avg > T2:
                    return np.median(base)
                else: return img_arr[i, j]
            else:
                template_size += 2
                if template_size > max_win:
                    template_size -= 2
                    #5
                    sum = 0
                    for k in range(template_size):
                        for l in range(template_size):
                            if k == center and l == center:
                                continue
                            else:
                                sum += np.abs(base[center, center] - base[k, l])
                    avg = sum / (template_size ** 2 - 1)
                    if avg > T2:
                        return np.median(base)
                    else:
                        return img_arr[i, j]
                else: continue





def mediumfilter_bn(img_arr, max_win, T1, T2):
    # 中值滤波器：
    # 将每一像素点的灰度值设置为该点某邻域窗口内的所有像素点灰度值的中值
    # img_arr->待处理图像arr形式
    # max_win -> 最大模板大小:得是奇数！！！>1
    # T1: 判定噪声点阈值1
    # T2: 判定噪声点阈值2
    height, width = img_arr.shape        # 图像长宽
    Gmax = np.max(img_arr)
    Gmin = np.min(img_arr)
    result = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            result[i][j] = judge(Gmax, Gmin, max_win, i, j, img_arr, T1, T2, height, width)
    # 返回结果
    return result.astype(np.uint8)

if __name__ == '__main__':
    # 对噪声图像进行处理
    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper1')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_bn(img_arr, 9, 10, 20)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_basenoise/c+saltpeper1+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper3')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_bn(img_arr, 9, 10, 20)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_basenoise/c+saltpeper3+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+saltpeper5')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_bn(img_arr, 9, 10, 20)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_basenoise/c+saltpeper5+medi.bmp")

    img, name = ShowImage.get_img("./img_noise/", 'c+gaussian')
    img_arr = Image2arr.image2arr(img)
    img_arr_medium = mediumfilter_bn(img_arr, 9, 10, 20)
    img_medium = Image2arr.arr2image(img_arr_medium)
    img_medium.save("./result_basenoise/c+gaussian+medi.bmp")