# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd
import numpy as np

students = pd.read_excel('C:/Temp/Students.xlsx')

# 追加列
students['Age'] = 25

# 删除列
students.drop(columns=['Score', 'Age'], inplace=True)

# 插入列
students.insert(1, column='Foo', value=np.repeat('foo', len(students)))

# 改列名
students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)

# 设置空值
students['ID'] = students['ID'].astype(float)
for i in range(5, 15):
    students['ID'].at[i] = np.nan

# 去掉空值
students.dropna(inplace=True)

print(students)
