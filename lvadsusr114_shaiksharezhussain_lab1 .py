# -*- coding: utf-8 -*-
"""LVADSUSR114_ShaikSharezHussain_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t6cDKaOniL90hHd0HTmA5q7P2xtrRlW_
"""

#1.5
import pandas as pd
import numpy as np
df=pd.read_csv('/content/winequality-red.csv')

df.head()

#a
#i
df.isnull().sum()
df1=df.ffill()

#ii
import matplotlib.pyplot as plt
plt.boxplot(df1)
plt.boxplot(df1['chlorides'])
plt.show()

#managing outliers
Q1 = np.percentile(df1, 25, axis=0)
Q3 = np.percentile(df1, 75, axis=0)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_lower = (df1 < lower_bound).any(axis=1)
outliers_upper = (df1 > upper_bound).any(axis=1)
outliers = outliers_lower | outliers_upper
df2 = df1[~outliers]

#b
df2['rating']="NA"
df2['rating']=np.where(df2['quality']>=3 & (df2['quality']<=6),"Good","Bad")

#c
from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
df2['rating']=lab.fit_transform(df2['rating'])

#d
#x=df2.drop('rating') #Removing the target variable and keeping rest..but we only take 2 features
x=df2[['alcohol','sulphates']]
y=df2['rating']

#e
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

#f
from sklearn.ensemble import RandomForestClassifier
ran=RandomForestClassifier()
ran.fit(x_train,y_train)
y_pred=ran.predict(x_test)

#g
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision
from sklearn.metrics import recall
acc=accuracy_score(y_pred,y_test)
prec=precision(y_pred,y_test)
rec=recall(y_pred,y_test)
print(acc,prec,rec)






