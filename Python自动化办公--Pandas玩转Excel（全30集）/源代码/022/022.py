# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd

students1 = pd.read_csv('C:/Temp/Students.csv', index_col='ID')
students2 = pd.read_csv('C:/Temp/Students.tsv', sep='\t', index_col='ID')
students3 = pd.read_csv('C:/Temp/Students.txt', sep='|', index_col='ID')

print(students1)
print(students2)
print(students3)
