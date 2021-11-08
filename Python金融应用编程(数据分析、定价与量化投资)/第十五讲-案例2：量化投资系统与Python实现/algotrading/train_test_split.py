# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区 
# @File : read.py
# @Software: PyCharm
# @Description: 
# 0基础如何系统的学会Python？ 链接：https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ

#train_test_split.py

from __future__ import print_function

import datetime

import sklearn
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.lda import LDA
from sklearn.metrics import confusion_matrix
from sklearn.qda import QDA
from sklearn.svm import LinearSVC,SVC

from create_lagged_series import create_lagged_series

if __name__=="__main__":
    snpret=create_lagged_series(
        "^GSPC",datetime.datetime(2001,1,10),
        datetime.datetime(2005,12,31),lags=5
    )
    X=snpret[["Lag1","Lag2"]]
    y=snpret["Direction"]
    
    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.8,random_state=42
    )
    print("Hit Rates/Confusion Matrices:\n")
    models=[("LR",LogisticRegression()),
            ("LDA",LDA()),
            ("QDA",QDA()),
            ("LSVC",LinearSVC()),
            ("RSVM",SVC(
                C=1000000.0,cache_size=200,class_weight=None,
                coef0=0.0,degree=3,gamma=0.0001,kernel='rbf',
                max_iter=-1,probability=False,random_state=None,
                shrinking=True,tol=0.001,verbose=False
            )),
            ("RF",RandomForestClassifier(
                n_estimators=1000,criterion='gini',
                max_depth=None,min_samples_split=2,
                min_samples_leaf=1,max_features='auto',
                bootstrap=True,oob_score=False,n_jobs=1,
                random_state=None,verbose=0
            ))]
    for m in models:
        m[1].fit(X_train,y_train)
        pred=m[1].predict(X_test)
        print("%s:\n%0.3f" % (m[0],m[1].score(X_test,y_test)))
        print("%s:\n" % confusion_matrix(pred,y_test))
