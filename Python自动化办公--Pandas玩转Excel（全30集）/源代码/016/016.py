# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd

# students = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Students')
# scores = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Scores')
# table = students.merge(scores, how='left', on='ID').fillna(0)
# table.Score = table.Score.astype(int)
# print(table)

# students = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Students', index_col='ID')
# scores = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Scores', index_col='ID')
# table = students.merge(scores, how='left', left_on=students.index, right_on=scores.index).fillna(0)
# table.Score = table.Score.astype(int)
# print(table)

students = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('C:/Temp/Student_score.xlsx', sheet_name='Scores', index_col='ID')
table = students.join(scores, how='left').fillna(0)
table.Score = table.Score.astype(int)
print(table)
