import numpy as np


def Identity(x):
    return x


def dropOut(x, d_scale):
    y = np.random.rand(x.shape[0], x.shape[1]) < d_scale
    y = np.multiply(y, 1 / d_scale)
    return np.multiply(x, y)


class Layer:
    def __init__(self):
        self.__numOfNode = []
        # 各层的神经元节点数量
        self.__hiddenLayer = []
        # 隐藏层
        self.__momentum = []
        # 动量
        self.__W = []
        # 权值
        self.__Input = None
        # 输入层
        self.__Output = None
        # 输出层
        self.__alpha = 0.9
        # 学习率

    # 获得权值
    def getW(self):
        return self.__W

    # 设置权值
    def setW(self, W: []):
        self.__W = W

    # 设置学习率
    def setAlpha(self, alpha):
        self.__alpha = alpha

    # 获得隐藏层
    def getHiddenLayer(self):
        return self.__hiddenLayer

    # 获得隐藏层数量
    def getNumOfHiddenLayer(self):
        return len(self.__numOfNode) - 2

    # 设置输入层
    def setInput(self, Input):
        self.__Input = Input

    # 设置输出层
    def setOutput(self, Output):
        self.__Output = Output

    # 获得输出层
    def getOutput(self):
        return self.__Output

    # 获得各层神经元节点数量
    def getNumOfNode(self):
        return self.__numOfNode

    # 设置各层神经元节点数量
    def setNumOfNode(self, numOfNode: []):
        self.__numOfNode = numOfNode
        for i in range(0, len(numOfNode) - 1):
            # 初始化权值和动量
            self.__W.append(np.random.random((numOfNode[i + 1], numOfNode[i])))
            self.__momentum.append(np.zeros((numOfNode[i + 1], numOfNode[i])))
        for i in range(1, len(numOfNode) - 1):
            # 初始化隐藏层
            self.__hiddenLayer.append(np.random.random((numOfNode[i], 1)))

    # 计算隐藏层各节点值
    def calculateHidden(self, d_scale, aFuncH=Identity):
        for i in range(0, self.getNumOfHiddenLayer()):
            if i == 0:
                # 第一层隐藏层通过输入层和第一层权值来计算
                v = np.dot(self.__W[0], self.__Input)
                y = aFuncH(v)
                z = dropOut(y, d_scale)
                self.__hiddenLayer[0] = z
            else:
                # 后面的隐藏层通过上一层隐藏层和对应权值来计算
                v = np.dot(self.__W[i], self.__hiddenLayer[i - 1])
                y = aFuncH(v)
                z = dropOut(y, d_scale)
                self.__hiddenLayer[i] = z

    # 计算输出层节点值
    def calculateOutPut(self, aFuncO=Identity):
        index = self.getNumOfHiddenLayer()
        # 获得隐藏层数量
        if index == 0:
            # 如果没有隐藏层则输出层由输入层和权值来计算
            v = np.dot(self.__W[0], self.__Input)
            y = aFuncO(v)
            self.__Output = y
        else:
            # 否则输出层由最后一层隐藏层和权值来计算
            v = np.dot(self.__W[index], self.__hiddenLayer[index - 1])
            y = aFuncO(v)
            self.__Output = y

    # 更新权值
    def updateW(self, d, dFuncH, dFuncO, m_scale):
        lenW = self.getNumOfHiddenLayer() + 1
        # 权值数组的长度为隐藏层数量 + 1

        e = [0] * lenW
        delta = [0] * lenW
        # 每层的 error 和 delta

        index = lenW - 1
        e[index] = d - self.__Output
        delta[index] = dFuncO(self.__Output, e[index])
        # 获得输出层的误差和delta
        index -= 1
        while index >= 0:
            # 获得隐藏层的误差和delta
            e[index] = np.dot(np.transpose(self.__W[index + 1]), delta[index + 1])
            delta[index] = dFuncH(self.__hiddenLayer[index], e[index])
            index -= 1

        # 计算输入层的动量
        self.__momentum[0] = (self.__alpha * delta[0] * np.transpose(self.__Input) * m_scale) + (
                self.__momentum[0] * (1 - m_scale))
        self.__W[0] += self.__momentum[0]
        # 更新第一层的权值
        for i in range(1, lenW):
            # 更新后面每一层的权值
            self.__momentum[i] = (self.__alpha * delta[i] * np.transpose(self.__hiddenLayer[i - 1]) * m_scale) + (
                    self.__momentum[i] * (1 - m_scale))
            self.__W[i] += self.__momentum[i]
