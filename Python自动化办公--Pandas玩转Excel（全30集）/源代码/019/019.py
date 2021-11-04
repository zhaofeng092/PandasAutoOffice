# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd

students = pd.read_excel('C:/Temp/Students.xlsx', index_col='ID')

row_sum = students[['Test_1', 'Test_2', 'Test_3']].sum(axis=1)
row_mean = students[['Test_1', 'Test_2', 'Test_3']].mean(axis=1)

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)
print(students)
