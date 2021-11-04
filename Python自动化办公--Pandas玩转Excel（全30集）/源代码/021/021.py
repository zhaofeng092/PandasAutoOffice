# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/s8SM69ioH_UJw_0Ytx8qvg

import pandas as pd

pd.options.display.max_columns = 999
videos = pd.read_excel('C:/Temp/Videos.xlsx', index_col='Month')
# table = videos.transpose()
table = videos.T
print(table)
