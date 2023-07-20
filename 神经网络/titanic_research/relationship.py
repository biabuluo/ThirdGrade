# -*-coding:utf-8 -*-
import pandas
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import seaborn as sns
sns.set_style("whitegrid")
"""
# File       : relationship
# Time       ：2023/5/29 15:41
# Author     ：chenyu
# version    ：python 3.8
# Description：特征相关性分析
"""

# 数据预处理
titanic = pandas.read_csv("train.csv")

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
titanic['Sex']=titanic['Sex'].apply(lambda x : int(x))
# 上船地点初始化
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 2
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 3
titanic['Embarked']=titanic['Embarked'].apply(lambda x : int(x))
# 删除无信息属性
titanic = titanic.drop(['Initial'], axis=1)
titanic = titanic.drop(['PassengerId'], axis=1)
titanic = titanic.drop(['Name'], axis=1)
titanic = titanic.drop(['Ticket'], axis=1)
titanic = titanic.drop(['Cabin'], axis=1)

print(titanic.head())
print(titanic.info())
# 写回csv文件
titanic.to_csv(r"titanic_train2.csv", index=False)

# 通过 Violin plot（小钢琴图）和 Pointplot（点图），分
# 别从数据分布和斜率，观察各特征与存活之间的关系：
# 设置颜色主题
antV = ['#1890FF', '#2FC25B', '#FACC14']
# 绘制 Violinplot 小钢琴图
f, axes = plt.subplots(2, 4, figsize=(8, 8), sharex=True)
sns.despine(left=True)
sns.violinplot(x='Survived', y='Pclass', data=titanic, palette=antV, ax=axes[0, 0])
sns.violinplot(x='Survived', y='Sex', data=titanic, palette=antV, ax=axes[0, 1])
sns.violinplot(x='Survived', y='Age', data=titanic, palette=antV, ax=axes[0, 2])
sns.violinplot(x='Survived', y='SibSp', data=titanic, palette=antV, ax=axes[0, 3])
sns.violinplot(x='Survived', y='Parch', data=titanic, palette=antV, ax=axes[1, 0])
sns.violinplot(x='Survived', y='Fare', data=titanic, palette=antV, ax=axes[1, 1])
sns.violinplot(x='Survived', y='Embarked', data=titanic, palette=antV, ax=axes[1, 2])
f.delaxes(axes[1][3])
plt.show()

# 绘制 pointplot 点图
f, axes = plt.subplots(2, 4, figsize=(8, 8), sharex=True)
sns.despine(left=True)
sns.pointplot(x='Survived', y='Pclass', data=titanic, color=antV[0], ax=axes[0, 0])
sns.pointplot(x='Survived', y='Sex', data=titanic, color=antV[0], ax=axes[0, 1])
sns.pointplot(x='Survived', y='Age', data=titanic, color=antV[0], ax=axes[0, 2])
sns.pointplot(x='Survived', y='SibSp', data=titanic, color=antV[0], ax=axes[0, 3])
sns.pointplot(x='Survived', y='Parch', data=titanic, color=antV[0], ax=axes[1, 0])
sns.pointplot(x='Survived', y='Fare', data=titanic, color=antV[0], ax=axes[1, 1])
sns.pointplot(x='Survived', y='Embarked', data=titanic, color=antV[0], ax=axes[1, 2])
f.delaxes(axes[1][3])
plt.show()

antV = ['#1890FF', '#2FC25B']
#生成各特征之间关系的矩阵图：
# sns.pairplot(data=titanic, palette=antV, hue= 'Survived')
# plt.show()

# 最后，通过热图找出数据集中不同特征之间的相关性，高正
# 值或负值表明特征具有高度相关性：
fig=plt.gcf()
fig.set_size_inches(12, 8)
fig=sns.heatmap(titanic.corr(), annot=True, cmap='GnBu', linewidths=1, linecolor='k', square=True, mask=False, vmin=-1, vmax=1, cbar_kws={"orientation": "vertical"}, cbar=True)
plt.show()
