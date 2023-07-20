# -*-coding:utf-8 -*-
import pandas as pd
"""
# File       : DataSplitter
# Time       ：2023/5/25 18:53
# Author     ：chenyu
# version    ：python 3.8
# Description：切割数据类
"""
class Splitter:
    # 读取数据
    def datareader(self, path):
        return pd.read_csv(path)

    # 数据乱序
    def datashuffle(self, df):
        return df.sample(frac=1)

    # 拆标签
    def splitlabel(self, df, labelname):
        attribute = df.drop([labelname], axis=1)
        label = df[labelname]
        return attribute, label

    # 拆分训练集测试集
    def splittest(self, df, ratio):
        train_size = int(len(df) * ratio)
        train = df[:train_size]
        test = df[:train_size]
        return train, test

    # 封装
    def splitter(self, path, ratio, labelname):
        data = self.datareader(path)
        data = self.datashuffle(data)
        train, test = self.splittest(data, ratio)
        train_x, train_y = self.splitlabel(train, labelname)
        test_x, test_y = self.splitlabel(test, labelname)
        return train_x, train_y, test_x, test_y

    def droper(self, path, ratio, labelname, dropname):
        train_x, train_y ,test_x, test_y = self.splitter(path, ratio, labelname)
        train_x = train_x.drop(dropname, axis=1)
        test_x = test_x.drop(dropname, axis=1)
        return train_x, train_y, test_x, test_y

    def droper_test(self, path, labelname, dropname):
        df = pd.read_csv(path)
        test_x = df.drop([labelname], axis=1)
        test_y = df[labelname]
        test_x = test_x.drop(dropname, axis=1)
        return test_x, test_y


if __name__ == '__main__':
    mysplitter = Splitter()

    droplist = ['Parch', 'P1', 'P2', 'P3', 'E1', 'E2', 'E3']
    # train_x, train_y, test_x, test_y = mysplitter.droper("titanic_train.csv",
    #                                                    1,
    #                                                    'Survived',
    #                                                      droplist)
    test_x, test_y = mysplitter.droper_test('titanic_test.csv',
                                            'Survived',
                                            droplist)
    print(test_x.head())
