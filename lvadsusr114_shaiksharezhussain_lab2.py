# -*- coding: utf-8 -*-
"""LVADSUSR114_ShaikSharezHussain_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BNG3r-r_lMjkKT4K3YF1RSkwCFHH-jJt
"""

#2.5
import pandas as pd
import numpy as np
df=pd.read_csv('/content/Mall_Customers.csv')
df

#a
df.isnull().sum()
#df['Annual Income (k$)'].fillna(df['Annual Income (k$)'].mean())
df1=df.ffill()

#feature Selection
x=df1[['Age','Annual Income (k$)']]
y=df1['Spending Score (1-100)']

#split dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

#normalization
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

#b
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
inertia=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i)
  kmeans.fit(x_train)
  inertia.append(kmeans.inertia_)
plt.plot(range(1,11),inertia)
#Optimal No of Clusters = 3 from ELbow method

#silhouetteScore
KMeans.score(x_test)

#c
import seaborn as sns
kmeans=KMeans(n_clusters=3)
kmeans.fit(x_train)
plt.scatter(df['Age'],df['Spending Score (1-100)'],c=kmeans.labels_)e

#d
print(kmeans.cluster_centers_)
kk=kmeans.fit_predict(x_train)
l=[]

#e
#The First Cluster is a high value Cluster..The Second Cluster has a mid level value
#We can suggest some Loyality programs to Allow the 3rd clusters from not churning