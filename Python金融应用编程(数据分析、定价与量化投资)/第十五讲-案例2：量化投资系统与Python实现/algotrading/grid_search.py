# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#grid_search.py

from __future__ import print_function

import datetime

import sklearn
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC

from create_lagged_series import create_lagged_series

if __name__=="__main__":
    snpret=create_lagged_series(
        "^GSPC",datetime.datetime(2001,1,10),
        datetime.datetime(2005,12,31), lags=5
    )
    X=snpret[["Lag1","Lag2"]]
    y=snpret["Direction"]
    
    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.5,random_state=42
    )
    tuned_parameters=[
        {'kernel':['rbf'],'gamma':[1e-3,1e-4],'C':[1,10,100,1000]}
    ]
    model=GridSearchCV(SVC(C=1),tuned_parameters,cv=10)
    model.fit(X_train,y_train)
    
    print("Optimised parameters found on training set:")
    print(model.best_estimator_,"\n")
    
    print("Grid scores calculated on training set:")
    for params,mean_score,scores in model.grid_scores_:
        print("%0.3f for %r" % (mean_score,params))
    