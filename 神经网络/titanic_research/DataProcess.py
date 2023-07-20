# -*-coding:utf-8 -*-
import pandas
"""
# File       : DataProcess
# Time       ：2023/5/24 21:37
# Author     ：chenyu
# version    ：python 3.8
# Description：数据处理
"""

# 数据预处理
titanic = pandas.read_csv("titanic_test.csv")
titanic.head(6)

# 年龄缺失值处理
# 填充
titanic.loc[:, 'Initial'] = 0  # 获取名字前缀
for i in titanic:
    titanic['Initial'] = titanic.Name.str.extract('([A-Za-z]+)\.')
for i in ['Rev', 'Sir', 'Mlle', 'Mme', 'Capt', 'Col',
        'Countess', 'Don', 'Dr', 'Jonkheer', 'Lady', 'Major', 'Ms']:
    titanic.loc[titanic["Initial"]==i, "Initial"] = 'Other'
titanic.loc[(titanic.Age.isnull())&(titanic.Initial=='Mr'), 'Age']=33
titanic.loc[(titanic.Age.isnull())&(titanic.Initial=='Mrs'), 'Age']=36
titanic.loc[(titanic.Age.isnull())&(titanic.Initial=='Master'), 'Age']=5
titanic.loc[(titanic.Age.isnull())&(titanic.Initial=='Miss'), 'Age']=22
titanic.loc[(titanic.Age.isnull())&(titanic.Initial=='Other'), 'Age']=46
# titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
titanic.head(6)

# 上船地点缺失值处理
titanic["Embarked"] = titanic["Embarked"].fillna('S')

# 性别数据初始化
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

# 上船地点初始化
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 2
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 3


# 对离散值one-hot编码：
# 对Pclass one-hot编码
titanic.loc[:, 'P1'] = 0
titanic.loc[:, 'P2'] = 0
titanic.loc[:, 'P3'] = 0
titanic.loc[titanic["Pclass"] == 1, "P1"] = 1
titanic.loc[titanic["Pclass"] == 2, "P2"] = 1
titanic.loc[titanic["Pclass"] == 3, "P3"] = 1
# 对Embarked one-hot编码
titanic.loc[:, 'E1'] = 0
titanic.loc[:, 'E2'] = 0
titanic.loc[:, 'E3'] = 0
titanic.loc[titanic["Embarked"] == 1, "E1"] = 1
titanic.loc[titanic["Embarked"] == 2, "E2"] = 1
titanic.loc[titanic["Embarked"] == 3, "E3"] = 1


# 删除无信息属性
titanic = titanic.drop(['Initial'], axis=1)
titanic = titanic.drop(['PassengerId'], axis=1)
titanic = titanic.drop(['Name'], axis=1)
titanic = titanic.drop(['Ticket'], axis=1)
titanic = titanic.drop(['Cabin'], axis=1)
titanic = titanic.drop(['Embarked'], axis=1)
titanic = titanic.drop(['Pclass'], axis=1)

# 写回csv文件
titanic.to_csv(r"titanic_test.csv", index=False)