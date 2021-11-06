# -*- coding: utf-8 -*-
# @公众号 :Web图书馆 代码详解：http://t.cn/A6Ihdrxf
# @Software: PyCharm 安装教程：https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q
# @Description:
# Python全套学习资源：https://mp.weixin.qq.com/s/G_5cY05Qoc_yCXGQs4vIeg

import pyodbc
import sqlalchemy
import pandas as pd

connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=(local); DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')
engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks?driver=SQL+Server')

query = 'SELECT FirstName, LastName FROM Person.Person'
df1 = pd.read_sql_query(query, connection)
df2 = pd.read_sql_query(query, engine)

pd.options.display.max_columns = 999
print(df1.head())
print(df2.head())
