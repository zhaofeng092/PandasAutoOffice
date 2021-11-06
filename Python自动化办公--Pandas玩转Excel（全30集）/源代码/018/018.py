# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pandas as pd

employees = pd.read_excel('C:/Temp/Employees.xlsx', index_col='ID')
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]
print(employees)
