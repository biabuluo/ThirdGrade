# -*-coding:utf-8 -*-
import numpy as np
import ShowImage
import Image2arr
"""
# File       : AddNoise2images
# Time       ：2023/6/13 21:07
# Author     ：chenyu
# version    ：python 3.8
# Description：给图像添加各种噪声
"""
def add_uniform_noise(img, low, high):
    # 均匀噪声函数
    # input；
    # img->图像经过numpy处理的结果（array）
    # low->下界   high->上界
    # output:
    # img_gaussian->图片加噪
    # noise->噪声图像
    noise = np.random.uniform(low, high, size=img.shape).astype('uint8')
    img_with_noise = img + noise
    np.clip(img_with_noise, 0, 255)
    return img_with_noise

def save_image_uniform(imgName, img_after_name, low, high):
    # 保存均匀噪声图像函数
    # input:
    # imgName->处理图像名称
    # img_after_name->处理后图像名称
    # noise_name->噪声图片
    # sigma->参数
    # output: void
    path = "./images/"
    img, name = ShowImage.get_img(path, imgName)
    img_arr = Image2arr.image2arr(img)
    # 噪声比例为proportion
    img_arr_noise = add_uniform_noise(img_arr, low, high)
    img_arr_addnoise = Image2arr.arr2image(img_arr_noise)
    # 保存图像
    image_path = "./img_noise/"
    img_arr_addnoise.save(image_path + img_after_name)

def add_gamma_noise(img, shape, scale):
    # 伽马噪声函数
    # input；
    # img->图像经过numpy处理的结果（array）
    # shape->gamma函数的形状     scale->尺度     （float）>0
    # output:
    # img_gaussian->图片加噪
    # noise->噪声图像
    noise = np.random.gamma(shape=shape, scale=scale, size=img.shape).astype('uint8')
    img_with_noise = img + noise
    np.clip(img_with_noise, 0, 255)
    return img_with_noise

def save_image_gamma(imgName, noise_name, shape, scale):
    # 保存伽马噪声图像函数
    # input:
    # imgName->处理图像名称
    # img_after_name->处理后图像名称
    # noise_name->噪声图片
    # sigma->参数
    # output: void
    path = "./images/"
    img, name = ShowImage.get_img(path, imgName)
    img_arr = Image2arr.image2arr(img)
    # 噪声比例为proportion
    img_arr_addnoise = add_gamma_noise(img_arr, shape, scale)
    img_arr_noise = Image2arr.arr2image(img_arr_addnoise)
    # 保存图像
    image_path = "./img_noise/"
    img_arr_noise.save(image_path + noise_name)


def add_rayleigh_noise(img, sigma):
    # 瑞利噪声函数
    # input；
    # img->图像经过numpy处理的结果（array）
    # sigma->添加噪声的参数
    # output:
    # img_gaussian->图片加噪
    # noise->噪声图像
    noise = np.random.rayleigh(sigma, img.shape).astype('uint8')
    img_with_noise = img + noise
    np.clip(img_with_noise, 0, 255)
    return img_with_noise

def save_image_rayleigh(imgName, noise_name, sigma):
    # 保存瑞利噪声图像函数
    # input:
    # imgName->处理图像名称
    # img_after_name->处理后图像名称
    # noise_name->噪声图片
    # sigma->参数
    # output: void
    path = "./images/"
    img, name = ShowImage.get_img(path, imgName)
    img_arr = Image2arr.image2arr(img)
    # 噪声比例为proportion
    img_arr_noise = add_poisson_noise(img_arr, sigma)
    img_arr_noise = Image2arr.arr2image(img_arr_noise)
    # 保存图像
    image_path = "./img_noise/"
    img_arr_noise.save(image_path + noise_name)

def add_poisson_noise(img, lamda):
    # 泊松噪声函数
    # input；
    # img->图像经过numpy处理的结果（array）
    # lamda->添加噪声的比例
    # output:
    # img_with_noise->图片加噪
    # noise->噪声图像
    noise = np.random.poisson(lamda, img.shape).astype('uint8')
    img_with_noise = img + noise    # 图像添加噪声
    np.clip(img_with_noise, 0, 255)     # 图像截断
    return img_with_noise

def save_image_poisson(imgName, noise_name, lamda):
    # 保存泊松噪声图像函数
    # input:
    # imgName->处理图像名称
    # img_after_name->处理后图像名称
    # noise_name->噪声图片
    # lamda->lamda越大，噪声程度越深
    # output: void
    path = "./images/"
    img, name = ShowImage.get_img(path, imgName)
    img_arr = Image2arr.image2arr(img)
    # 噪声比例为proportion
    img_arr_addnoise = add_poisson_noise(img_arr, lamda)
    img_arr_noise = Image2arr.arr2image(img_arr_addnoise)
    # 保存图像
    image_path = "./img_noise/"
    img_arr_noise.save(image_path + noise_name)

def add_gaussian_noise(img, sigma):
    # 高斯噪声函数
    # input:
    # img->图像经过numpy处理的结果（array）
    # siama->标准差参数
    # output:
    # img_gaussian->图片高斯加噪
    # noise->噪声图像
    # img = img / 255     # 图片灰度标准化
    noise = np.random.normal(0, sigma, img.shape)   # 产生高斯噪声  均值设为0
    img_gaussian = img + noise       # 将噪声与图片叠加处理
    img_gaussian = np.clip(img_gaussian, 0, 255)    # 图像截断
    # 灰度范围设置为0-255 转为uint8类型
    img_gaussian = img_gaussian.astype(dtype=np.uint8)
    return img_gaussian


def save_image_gaussian(imgName, noise_name, sigma):
    # 保存高斯噪声图像函数
    # input:
    # imgName->处理图像名称
    # img_after_name->处理后图像名称
    # noise_name->噪声图片
    # sigma->标准差
    # output: void
    path = "./images/"
    img, name = ShowImage.get_img(path, imgName)
    img_arr = Image2arr.image2arr(img)
    # 标准差设为sigma
    img_arr_addnoise = add_gaussian_noise(img_arr, sigma)
    img_arr_noise = Image2arr.arr2image(img_arr_addnoise)
    # 保存图像
    image_path = "./img_noise/"
    img_arr_noise.save(image_path + noise_name)

def add_saltpepper_noise(img, proportion):
    # 椒盐噪声函数
    # input；
    # img->图像经过numpy处理的结果（array）
    # proportion->添加噪声的比例
    # output:
    # img_gaussian->图片椒盐加噪
    # noise->噪声图像
    image_copy = img.copy()
    img_Y, img_X = img.shape        # 求得其高宽
    X = np.random.randint(img_X, size=(int(proportion * img_X * img_Y),))       # 噪声点的 X 坐标
    Y = np.random.randint(img_Y, size=(int(proportion * img_X * img_Y),))       # 噪声点的 Y 坐标
    image_copy[Y, X] = np.random.choice([0, 255], size=(int(proportion * img_X * img_Y),))          # 噪声点的坐标赋值
    sp_noise_plate = np.ones_like(image_copy) * 127       # 噪声容器
    sp_noise_plate[Y, X] = image_copy[Y, X]               # 将噪声给噪声容器
    return image_copy, sp_noise_plate


def save_image_saltpeper(imgName, img_after_name, proportion):
    # 保存椒盐噪声图像函数
    # input:
    # imgName->处理图像名称
    # img_after_name->处理后图像名称
    # noise_name->噪声图片
    # proportion->噪声比例
    # output: void
    path = "./images/"
    img, name = ShowImage.get_img(path, imgName)
    img_arr = Image2arr.image2arr(img)
    # 噪声比例为proportion
    img_arr_addnoise, img_arr_noise = add_saltpepper_noise(img_arr, proportion)
    img_arr_addnoise = Image2arr.arr2image(img_arr_addnoise)
    img_arr_noise = Image2arr.arr2image(img_arr_noise)
    # 保存图像
    image_path = "./img_noise/"
    img_arr_addnoise.save(image_path + img_after_name)


if __name__ == '__main__':
    # 生成不同图像的不同比例的椒盐噪声
    # Cameraman     # 保存图像
    save_image_saltpeper("Cameraman", "c+saltpeper1.bmp", 0.1)
    save_image_saltpeper("Cameraman", "c+saltpeper3.bmp", 0.3)
    save_image_saltpeper("Cameraman", "c+saltpeper5.bmp", 0.5)


    # 生成不同图像的高斯噪声
    # 保存图像
    save_image_gaussian("Cameraman", "c+gaussian.bmp", 50)


    # 生成不同噪声图像
    # Cameraman     # 保存图像
    # save_image_gaussian("Cameraman", "c+gaussian.bmp", 25)
    # save_image_saltpeper("Cameraman", "c+saltpeper.bmp", 0.1)
    # save_image_poisson("Cameraman", "c+poisson.bmp", 60)
    # save_image_gamma("Cameraman", "c+gamma.bmp", 7, 7)
    # save_image_rayleigh("Cameraman", "c+rayleigh.bmp", 70.0)
    # save_image_uniform("Cameraman", "c+uniform.bmp", 50, 100)