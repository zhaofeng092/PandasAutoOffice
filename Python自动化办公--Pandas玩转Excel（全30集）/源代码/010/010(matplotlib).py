# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values(by='2015 to 16', inplace=True, ascending=False)
students.index = range(0, len(students))
print(students)

bar_width = 0.7
x_pos = np.arange(len(students) * 2, step=2)
plt.bar(x_pos, students['2016 to 17'], color='green', width=bar_width)
plt.bar(x_pos + bar_width, students['2015 to 16'], color='blue', width=bar_width)

plt.xticks(x_pos + bar_width / 2, students['Field'], rotation='90')
plt.title('International Student by Field', fontsize=16)
plt.xlabel('Field')
plt.ylabel('Number')
plt.tight_layout()
plt.show()
