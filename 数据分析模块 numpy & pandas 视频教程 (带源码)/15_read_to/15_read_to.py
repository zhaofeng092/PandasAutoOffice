 
"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
import pandas as pd

# read from
data = pd.read_csv('student.csv')
print(data)

# save to
data.to_pickle('student.pickle')