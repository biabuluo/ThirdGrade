# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import numpy as np
import pandas as pd

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    # 对数据进行乱序处理
    data = pd.read_csv("titanic_train.csv")
    data_shuffled = data.sample(frac=1)

    # print(data_shuffled.head())

    # 拆分标签
    attribute = data_shuffled.drop(['Survived'], axis=1)
    label = data_shuffled['Survived']

    # 划分训练集、测试集 8:2
    train_size = int(len(attribute)*0.8)
    train_x = attribute[:train_size]
    train_y = label[:train_size]
    test_x = attribute[train_size:]
    test_y = label[train_size:]

    # for i in zip(test_y.values, test_y.values):
    print(test_x.shape)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
