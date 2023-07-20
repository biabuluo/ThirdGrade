# -*-coding:utf-8 -*-
from DataSplitter import Splitter
import tensorflow as tf
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False
"""
# File       : layerchoose
# Time       ：2023/5/25 22:07
# Author     ：chenyu
# version    ：python 3.8
# Description：比较层数不同
"""


# 建立Keras序列模型
mynn1 = keras.models.Sequential()
mynn2 = keras.models.Sequential()
mynn3 = keras.models.Sequential()
mynn4 = keras.models.Sequential()

# 第一层
mynn1.add(keras.layers.Dense(units=64, input_dim=11, use_bias=True,
                            kernel_initializer='uniform',
                            bias_initializer='zeros',
                            activation='relu'))
mynn2.add(keras.layers.Dense(units=64, input_dim=11, use_bias=True,
                            kernel_initializer='uniform',
                            bias_initializer='zeros',
                            activation='relu'))
mynn3.add(keras.layers.Dense(units=64, input_dim=11, use_bias=True,
                            kernel_initializer='uniform',
                            bias_initializer='zeros',
                            activation='relu'))
mynn4.add(keras.layers.Dense(units=64, input_dim=11, use_bias=True,
                            kernel_initializer='uniform',
                            bias_initializer='zeros',
                            activation='relu'))
# 第二层
mynn2.add(keras.layers.Dense(units=32, activation='relu'))
mynn3.add(keras.layers.Dense(units=32, activation='relu'))
mynn4.add(keras.layers.Dense(units=32, activation='relu'))

# 第三层
mynn3.add(keras.layers.Dense(units=16, activation='relu'))
mynn4.add(keras.layers.Dense(units=16, activation='relu'))

# 第四层
mynn4.add(keras.layers.Dense(units=16, activation='relu'))

# 输出层
mynn1.add(keras.layers.Dense(units=1, activation='sigmoid'))
mynn2.add(keras.layers.Dense(units=1, activation='sigmoid'))
mynn3.add(keras.layers.Dense(units=1, activation='sigmoid'))
mynn4.add(keras.layers.Dense(units=1, activation='sigmoid'))

# 模型设置
mynn1.compile(optimizer=tf.keras.optimizers.Adam(0.003),
             loss='binary_crossentropy',
             metrics=[keras.metrics.binary_accuracy])
mynn2.compile(optimizer=tf.keras.optimizers.Adam(0.003),
             loss='binary_crossentropy',
             metrics=[keras.metrics.binary_accuracy])
mynn3.compile(optimizer=tf.keras.optimizers.Adam(0.003),
             loss='binary_crossentropy',
             metrics=[keras.metrics.binary_accuracy])
mynn4.compile(optimizer=tf.keras.optimizers.Adam(0.003),
             loss='binary_crossentropy',
             metrics=[keras.metrics.binary_accuracy])

# 记录测试集最后的准确率
record_acc1 = []
record_acc2 = []
record_acc3 = []
record_acc4 = []

# 每个模型训练20次记录测试集准确率
for i in range(20):
    # 数据切割
    mysplitter = Splitter()
    train_x, train_y, test_x, test_y = mysplitter.splitter("titanic_train.csv",
                                                           0.8,
                                                           'Survived')
    history = mynn1.fit(train_x, train_y,
                       epochs=100,
                       batch_size=10,
                       validation_split=0.2,
                       verbose=2)
    loss, acc = mynn1.evaluate(test_x.values, test_y.values)
    record_acc1.append(acc)

for i in range(20):
    # 数据切割
    mysplitter = Splitter()
    train_x, train_y, test_x, test_y = mysplitter.splitter("titanic_train.csv",
                                                           0.8,
                                                           'Survived')
    history = mynn2.fit(train_x, train_y,
                       epochs=100,
                       batch_size=10,
                       validation_split=0.2,
                       verbose=2)
    loss, acc = mynn2.evaluate(test_x.values, test_y.values)
    record_acc2.append(acc)

for i in range(20):
    # 数据切割
    mysplitter = Splitter()
    train_x, train_y, test_x, test_y = mysplitter.splitter("titanic_train.csv",
                                                           0.8,
                                                           'Survived')
    history = mynn3.fit(train_x, train_y,
                        epochs=100,
                        batch_size=10,
                        validation_split=0.2,
                        verbose=2)
    loss, acc = mynn3.evaluate(test_x.values, test_y.values)
    record_acc3.append(acc)

for i in range(20):
    # 数据切割
    mysplitter = Splitter()
    train_x, train_y, test_x, test_y = mysplitter.splitter("titanic_train.csv",
                                                           0.8,
                                                           'Survived')
    history = mynn4.fit(train_x, train_y,
                        epochs=100,
                        batch_size=10,
                        validation_split=0.2,
                        verbose=2)
    loss, acc = mynn4.evaluate(test_x.values, test_y.values)
    record_acc4.append(acc)


# 去掉极端值
def my_AVERAGE_main(data_list):
    if len(data_list) == 0:
        return 0
    if len(data_list) > 2:
        data_list.remove(min(data_list))
        data_list.remove(max(data_list))
        average_data = float(sum(data_list)) / len(data_list)
        return average_data
    elif len(data_list) <= 2:
        average_data = float(sum(data_list)) / len(data_list)
        return average_data

# 计算四个模型的平均值
print(my_AVERAGE_main(record_acc1))
print(my_AVERAGE_main(record_acc2))
print(my_AVERAGE_main(record_acc3))
print(my_AVERAGE_main(record_acc4))

# 可视化


plt.plot(record_acc1)
plt.plot(record_acc2)
plt.plot(record_acc3)
plt.plot(record_acc4)
plt.title('diff layer accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['mynn1', 'mynn2', 'mynn3', 'mynn4'], loc='upper left')
plt.show()

