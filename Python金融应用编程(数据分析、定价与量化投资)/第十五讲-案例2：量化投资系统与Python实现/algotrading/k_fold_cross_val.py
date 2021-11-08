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
from sklearn import cross_validation
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
    
    kf=cross_validation.KFold(
        len(snpret),n_folds=10,indices=False,
        shuffle=True,random_state=42
    )
    for train_index,test_index in kf:
        X_train=X.ix[X.index[train_index]]
        X_test=X.ix[X.index[test_index]]
        y_train=y.ix[y.index[train_index]]
        y_test=y.ix[y.index[test_index]]
        print("Hit Rates/Confusion Matrices:\n")
        model=SVC(
                C=1000000.0,cache_size=200,class_weight=None,
                coef0=0.0,degree=3,gamma=0.0001,kernel='rbf',
                max_iter=-1,probability=False,random_state=None,
                shrinking=True,tol=0.001,verbose=False
            )
        model.fit(X_train,y_train)
        pred=model.predict(X_test)
        print("%0.3f" % model.score(X_test,y_test))
        print("%s:\n" % confusion_matrix(pred,y_test))
