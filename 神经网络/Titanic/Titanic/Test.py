import numpy as np
import Func as funs
import pandas
from NN import NN
from DataSplitter import DataSplitter
from sklearn.feature_extraction import DictVectorizer

# 数据读取切割
mysplitter = DataSplitter()
x_train, y_train, x_test, y_test = mysplitter.splitter("titanic_train.csv", 0.8, 'Survived')


# 构建神经网络
nn = NN()
nn.setAlpha(0.01)
nn.setNumOfNode([11, 40, 1])
nn.setX_Train(x_train)
nn.setY_Train(y_train)

# 训练神经网络
for i in range(0, 10000):
    if i % 100 == 0:
        print(str(i/100)+'%')
    cost = nn.SDG(funs.ReLu, funs.Sigmoid, funs.ReLu, funs.SigmoidCEDelta, m_scale=0.8)


# 预测测试集
nn.setX_Test(x_train)
predict_test = nn.predictTest(funs.ReLu, funs.Sigmoid)
print(predict_test)

for i in range(0, len(predict_test)):
    if predict_test[i] > 0.5:
        predict_test[i] = 1
    else:
        predict_test[i] = 0

# 计算正确率
diff = 0
for i in range(0, len(predict_test)):
    if predict_test[i] != y_train[i]:
        diff += 1
print(1 - diff / len(predict_test))
