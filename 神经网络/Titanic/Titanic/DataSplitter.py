# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
"""
# File       : DataSplitter
# Time       ：2023/5/24 18:47
# Author     ：chenyu
# version    ：python 3.8
# Description： 数据切割
"""

class DataSplitter:
    # 读取csv文件
    def datareader(self, path):
        self.__data = pd.read_csv(path)

    # 按比例切割数据 ratio：训练集占比
    def datasplit(self, ratio):
        length = len(self.__data)
        train_set = self.__data.loc[0: int(length*ratio)]
        test_set = self.__data.loc[int(length*ratio)+1: length-1]
        return train_set, test_set


    # 数据切割标签
    def labelsplit(self, data, label):
        attribute = data.drop([label], axis=1)
        label = data[label]
        return attribute, label

    # 使数据符合模型规范
    def regulardata(self, attribute, label):
        x_train = np.mat(attribute.values)
        y_train = np.transpose(np.mat(label.values))
        return x_train, y_train

    # 再封装
    def splitter(self, path, ratio, label):
        self.datareader(path)
        train_set, test_set =  self.datasplit(ratio)
        train_set_attributes, train_set_label = self.labelsplit(train_set, label)
        test_set_attributes, test_set_label = self.labelsplit(test_set, label)
        train_set_attributes, train_set_label = self.regulardata(train_set_attributes,
                                                                 train_set_label)
        test_set_attributes, test_set_label = self.regulardata(test_set_attributes,
                                                                 test_set_label)
        # 顺序输出训练集特征、训练集标签、测试集特征、测试集标签
        return train_set_attributes, train_set_label, test_set_attributes, test_set_label

    # 打乱函数
    def random_shuffle(self, data, label):
        dataset = np.hstack((data, label))
        np.random.seed(12345)
        np.random.shuffle(dataset)
        return dataset[:, :-1], dataset[:, -1]




if __name__ == '__main__':
    # mysplitter = DataSplitter()
    # train_x, train_y, test_x, test_y = mysplitter.splitter("titanic_train.csv", 0.8, 'Survived')
    # print(train_x.shape)
    # print('-------------')
    # print(train_y.shape)
    # train_x, train_y = mysplitter.random_shuffle(train_x, train_y)
    # print(train_x.shape)
    # print('-------------')
    # print(train_y.shape)
    import matplotlib.pyplot as plt
    import seaborn as sns
    import matplotlib
    plt.style.use('ggplot')
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    x = [1,2,3,4,5]
    y = [7,4,8,9,1]
    sns.lineplot(x=x, y=y)
    plt.show()




