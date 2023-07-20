# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 11:05
# @Author  : YJH
# @FileName: NN.py
# @Software: PyCharm

import numpy as np
from Layer import Layer


class NN:
    def __init__(self):
        self.__x_train = []
        self.__y_train = []
        # 训练集
        self.__x_test = []
        self.__y_test = []
        # 测试集
        self.__layer = Layer()
        # 神经网络中的层次

    # 获得权值
    def getW(self):
        return self.__layer.getW()

    def getCost(self, d, eFunc):
        return eFunc(d, self.__layer.getOutput())

    # 设置训练集数据
    def setX_Train(self, x_train):
        self.__x_train = x_train

    # 设置训练集标签
    def setY_Train(self, y_train):
        self.__y_train = y_train

    # 设置测试集数据
    def setX_Test(self, x_test):
        self.__x_test = x_test

    # 设置测试集标签
    def setY_Test(self, y_test):
        self.__y_test = y_test

    # 设置各个层次的神经元节点数量
    # 包括输入层、隐藏层和输出层
    def setNumOfNode(self, numOfNode: []):
        self.__layer.setNumOfNode(numOfNode)

    # 设置学习率
    def setAlpha(self, alpha):
        self.__layer.setAlpha(alpha)

    # SGD训练所有训练集样本
    def SDG(self, aFuncH, aFuncO, dFuncH, dFuncO, m_scale=1.0, d_scale=1.0):
        for i in range(0, len(self.__y_train)):
            self.__layer.setInput(np.transpose(self.__x_train[i]))
            self.__layer.calculateHidden(d_scale, aFuncH)
            self.__layer.calculateOutPut(aFuncO)
            self.__layer.updateW(np.transpose(self.__y_train[i]), dFuncH, dFuncO, m_scale)

    # 对测试集数据进行预测
    def predictTest(self, aFunH, aFuncO, d_scale=1):
        self.__y_test = []
        for i in range(0, len(self.__x_test)):
            self.__layer.setInput(np.transpose(self.__x_test[i]))
            self.__layer.calculateHidden(d_scale, aFunH)
            self.__layer.calculateOutPut(aFuncO)
            self.__y_test.append(self.__layer.getOutput())
        return self.__y_test
