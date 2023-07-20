import numpy as np


# 代价函数
def SSE(d, y):
    return np.power(np.subtract(d, y), 2) / 2

def CE(d, y):
    return -(d * np.log(y)) - ((1 - d) * np.log(1 - y))


# 激活函数
def Softmax(x):
    Max = np.max(x)
    exp = np.exp(x - Max)
    return exp / sum(exp)


def Sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLu(x):
    return np.maximum(0, x)


def SigmoidSSEDelta(y, e):
    temp = np.multiply(y, 1 - y)
    return np.multiply(temp, e)


def SigmoidCEDelta(y, e):
    return e


def SoftmaxCEDelta(y, e):
    return e


def ReLuCEDelta(y, e):
    return np.multiply((y > 0), e)
