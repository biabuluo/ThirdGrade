# -*-coding:utf-8 -*-

"""
# File       : Main
# Time       ：2023/6/13 21:13
# Author     ：chenyu
# version    ：python 3.8
# Description：调试程序
"""
from ex import ShowImage

if __name__ == '__main__':
    # 显示四种不同滤波器对噪声图像的处理
    imageNamelist = ["c+gaussian",
                     "c+gaussian+b",
                     "c+gaussian+g",
                     "c+gaussian+mean",
                     "c+gaussian+medi",
                     "c+saltpeper1",
                     "c+saltpeper1+b",
                     "c+saltpeper1+g",
                     "c+saltpeper1+mean",
                     "c+saltpeper1+medi"]
    imagePaths = ["./img_noise/",
                  "./result/",
                  "./result/",
                  "./result/",
                  "./result/",
                  "./img_noise/",
                  "./result/",
                  "./result/",
                  "./result/",
                  "./result/"]
    ShowImage.show_multi_images(2, 5, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )


    # 高比例椒盐噪声和传统中值滤波处理结果
    imageNamelist = ["c+saltpeper3",
                     "c+saltpeper3+medi",
                     "c+saltpeper5",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./result/",
                  "./img_noise/",
                  "./result/"]
    ShowImage.show_multi_images(2, 2, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )

    # 简单自适应中值定理处理结果
    imageNamelist = ["c+gaussian",
                     "c+saltpeper1",
                     "c+saltpeper3",
                     "c+saltpeper5",
                     "c+gaussian+medi",
                     "c+saltpeper1+medi",
                     "c+saltpeper3+medi",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./result_simple/",
                  "./result_simple/",
                  "./result_simple/",
                  "./result_simple/",]
    ShowImage.show_multi_images(2, 4, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )


    # x型自适应中值定理
    imageNamelist = ["c+gaussian",
                     "c+saltpeper1",
                     "c+saltpeper3",
                     "c+saltpeper5",
                     "c+gaussian+medi",
                     "c+saltpeper1+medi",
                     "c+saltpeper3+medi",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./result_x/",
                  "./result_x/",
                  "./result_x/",
                  "./result_x/"]
    ShowImage.show_multi_images(2, 4, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )

    # 九窗口自适应中值定理
    imageNamelist = ["c+gaussian",
                     "c+saltpeper1",
                     "c+saltpeper3",
                     "c+saltpeper5",
                     "c+gaussian+medi",
                     "c+saltpeper1+medi",
                     "c+saltpeper3+medi",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./result_9w/",
                  "./result_9w/",
                  "./result_9w/",
                  "./result_9w/"]
    ShowImage.show_multi_images(2, 4, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )


    # 基于噪声检测的自适应中值滤波处理结果
    imageNamelist = ["c+gaussian",
                     "c+saltpeper1",
                     "c+saltpeper3",
                     "c+saltpeper5",
                     "c+gaussian+medi",
                     "c+saltpeper1+medi",
                     "c+saltpeper3+medi",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./result_basenoise/",
                  "./result_basenoise/",
                  "./result_basenoise/",
                  "./result_basenoise/"]
    ShowImage.show_multi_images(2, 4, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )


    # 双边-自适应中值滤波处理结果
    imageNamelist = ["c+gaussian",
                     "c+saltpeper1",
                     "c+saltpeper3",
                     "c+saltpeper5",
                     "c+gaussian+medi",
                     "c+saltpeper1+medi",
                     "c+saltpeper3+medi",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./result_bil/",
                  "./result_bil/",
                  "./result_bil/",
                  "./result_bil/"]
    ShowImage.show_multi_images(2, 4, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )

    # 改进九窗口自适应处理结果（效果不太好）
    imageNamelist = ["c+gaussian",
                     "c+saltpeper1",
                     "c+saltpeper3",
                     "c+saltpeper5",
                     "c+gaussian+medi",
                     "c+saltpeper1+medi",
                     "c+saltpeper3+medi",
                     "c+saltpeper5+medi"]
    imagePaths = ["./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./img_noise/",
                  "./result_9w_ad/",
                  "./result_9w_ad/",
                  "./result_9w_ad/",
                  "./result_9w_ad/"]
    ShowImage.show_multi_images(2, 4, ShowImage.get_imags(imagePaths, imageNamelist)[0], imageNamelist, 5 )
