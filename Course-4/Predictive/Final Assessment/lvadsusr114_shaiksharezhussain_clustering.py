# -*- coding: utf-8 -*-
"""LVADSUSR114_ShaikSharezHussain_Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18XScuT0vFAGhA7as4Sgi2o4ae-1gJvtv
"""

#1
#Read Data
import pandas as pd
import numpy as np
df=pd.read_csv('/content/seeds.csv')
df

#2
#Data Pre-Processing
df.isnull().sum()

df=df.dropna()
#to remove duplicates which is not needed here as there are no null values

#df=df.fillna(df.mean())

#Outliers
import matplotlib.pyplot as plt
plt.boxplot(df)
plt.show()

plt.boxplot(df['Area'])

#removing Outliers
Q1 = np.percentile(df, 25, axis=0)
Q3 = np.percentile(df, 75, axis=0)
Q1 = np.percentile(df, 25, axis=0)
Q3 = np.percentile(df, 75, axis=0)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_lower = (df < lower_bound).any(axis=1)
outliers_upper = (df > upper_bound).any(axis=1)
outliers = outliers_lower | outliers_upper
df1 = df[~outliers]

#3
#Exploratory Data Analysis
df.info()

df.describe()

df.shape

df.head(5)

df.corr()

#4
#Model Training and Tesing
#feature selection
import seaborn as sns
sns.heatmap(df.corr())

#Normalizing
from sklearn.preprocessing import StandardScaler
x_train=df
scaler = StandardScaler()
x = scaler.fit_transform(x_train)

#split dataset
#from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

#Elbow Method for finding Optimal Clusters
from sklearn.cluster import KMeans
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(x)
    inertia.append(kmeans.inertia_)
plt.plot(range(1,11),inertia)

#optimal cluster=2
import seaborn as sns
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(x)
sns.scatterplot(data=df,x='Area',y='Perimeter',hue=kmeans.labels_)

#optimal cluster=3
import seaborn as sns
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(x)
sns.scatterplot(data=df,x='Area',y='Perimeter',hue=kmeans.labels_)

#mOdel Evaluation
score=silhouttescore(kmeans.labels_)