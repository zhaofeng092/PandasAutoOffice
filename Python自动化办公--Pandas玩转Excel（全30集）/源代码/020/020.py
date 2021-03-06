# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd

students = pd.read_excel('C:/Temp/Students_Duplicates.xlsx')
dupe = students.duplicated(subset='Name')
dupe = dupe[dupe == True]  # dupe = dupe[dupe]
print(students.iloc[dupe.index])
print("=========")
students.drop_duplicates(subset='Name', inplace=True, keep='last')
print(students)
