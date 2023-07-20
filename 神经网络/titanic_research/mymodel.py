# -*-coding:utf-8 -*-
import pandas as pd
import time
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
# File       : tensorflow
# Time       ：2023/5/24 21:47
# Author     ：chenyu
# version    ：python 3.8
# Description： 使用keras搭建神经网络
"""
# 数据切割
mysplitter = Splitter()
# train_x, train_y, test_x, test_y = mysplitter.splitter("titanic_train.csv",
#                                                        1,
#                                                        'Survived')
# df = pd.read_csv('titanic_test.csv')
# test_x = df.drop(['Survived'], axis=1)
# test_y = df['Survived']
# print(type(train_x))
# print(test_y)

# 对输入数据降维
# 保留属性：性别、年龄、船票价格、兄弟姐妹SibSp：
droplist = ['Parch', 'P1', 'P2', 'P3', 'E1', 'E2', 'E3']
train_x, train_y, test_x, test_y = mysplitter.droper("titanic_train.csv",
                                                     1,
                                                     'Survived',
                                                     droplist)
test_x, test_y = mysplitter.droper_test('titanic_test.csv',
                                        'Survived',
                                        droplist)
# print(test_y.values)

# 建立Keras序列模型
mynn = keras.models.Sequential()
# 第一层
mynn.add(keras.layers.Dense(units=32, input_dim=4, use_bias=True,
                            kernel_initializer='uniform',
                            bias_initializer='zeros',
                            activation='relu'))
# # 使用leaky relu
# mynn.add(keras.layers.LeakyReLU(0.1))
# # 使用dropout
# mynn.add(keras.layers.Dropout(0.2))
# 第二层
mynn.add(keras.layers.Dense(units=16, activation='relu'))
# # 使用leaky relu
# mynn.add(keras.layers.LeakyReLU(0.05))
# # 使用dropout
# mynn.add(keras.layers.Dropout(0.2))
# 输出层
mynn.add(keras.layers.Dense(units=1, activation='sigmoid'))

# 查看模型
# print(mynn.summary())
myoptimizer = tf.keras.optimizers.Adam(0.0001)
# sgd = keras.optimizers.SGD(lr=0.003, momentum=0, decay=0.0, nesterov=False)
# 模型设置
mynn.compile(optimizer=myoptimizer,
             loss='binary_crossentropy',
             metrics=[keras.metrics.binary_accuracy])

t1 = time.time()
# 模型训练
history = mynn.fit(train_x, train_y,
         epochs=1000,
         batch_size=10,
         validation_split=0.2,
         verbose=2)
t2 = time.time()

print('---------------------')
# print(history.epoch)
# print(history.history)
print('---------------------')
# 损失曲线可视化
# 绘制训练 & 验证的准确率值
f, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(history.history['binary_accuracy'])
ax[0].plot(history.history['val_binary_accuracy'])
ax[0].set_title('Model accuracy')
ax[0].set_ylabel('Accuracy')
ax[0].set_xlabel('Epoch')
# ax[0].legend(['Train', 'Test'], loc='upper left')
# plt.show()

# 绘制训练 & 验证的损失值
ax[1].plot(history.history['loss'])
ax[1].plot(history.history['val_loss'])
ax[1].set_title('Model loss')
ax[1].set_ylabel('Loss')
ax[1].set_xlabel('Epoch')
f.legend(['Train', 'Val'], loc='upper left')
plt.tight_layout()
plt.show()
#
# # 评估模型
print('----------------------')
print(mynn.evaluate(test_x.values, test_y.values))
print('程序运行时间:%s毫秒' % ((t2 - t1)*1000))







