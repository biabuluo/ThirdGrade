# -*-coding:utf-8 -*-
import pandas as pd
"""
# File       : testprocess
# Time       ：2023/5/26 19:08
# Author     ：chenyu
# version    ：python 3.8
# Description： 处理一下测试集数据
"""
df_data = pd.read_csv('test.csv')
df_label = pd.read_csv('submission (1).csv')

df_data['Survived'] = df_label['Survived']
print(df_data.head())
# 写回csv文件
df_data.to_csv(r"titanic_test.csv", index=False)