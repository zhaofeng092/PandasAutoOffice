# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd


def validate_age(a):
    return 18 <= a <= 30


def level_b(s):
    return 60 <= s < 90


students = pd.read_excel('C:/Temp/Students.xlsx', index_col='ID')
students = students.loc[students['Age'].apply(validate_age)].loc[students.Score.apply(level_b)]  # 两种语法
print(students)
