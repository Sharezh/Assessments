# -*- coding: utf-8 -*-
"""LVADSUSR114-ShaikSharezHussain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10zIdd5kZLVKEHiKNAYXmQoq8MXiKON_G
"""

#1
import numpy as np
import pandas as pd
rgb=np.array([[[255,0,0],[0,255,0],[0,0,255]],
              [[255,0,0],[255,0,255],[0,255,255]],
              [[127,127,127],[200,200,200],[50,50,50]]])
#print(rgb)
pro=np.array([0.2989,0.5870,0.1140])
print(np.multiply(rgb[0],pro[0]))
print(np.multiply(rgb[1],pro[1]))
print(np.multiply(rgb[1],pro[2]))

#2
a=np.array([168,100,26])
print(a.mean())
print(a.std())

#3
a=np.array([[[76,0,0],[0,76,0],[0,0,76]],
              [[149,0,0],[149,0,149],[0,149,149]],
              [[29,0,0],[29,0,29],[0,29,29]]])
a
a.flatten('C')
a.reshape(9,3)

#4
a=np.array([[3,1,4],[4,7,1],[7,8,9]])
df=pd.DataFrame(a)
df.corr()

#5
a=np.array([[89,91,54],[84,77,61],[67,88,69]])
print(a[0].mean())
print(a[1].mean())
print(a[2].mean())

#6
a=np.array([[3,1,4],[4,7,1],[7,8,9]])
b=np.array([2,5,4,21,23,6])
b.reshape(3,2)
def res(a,b):
  if(a[0]==b[0]):
    return a[0]
  return b[0]
c=res(a,b)
c.flatten()

#7
data={'Name':['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
      'Age':[25,30,35,40,45,50,55],
      'City':['NewYork','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston'],
      'Department':['HR','IT','Finance','Marketing','Sales','IT','HR']
      }
df=pd.DataFrame(data)
df2=df['Age']<45
df3=df['Department']!='HR'
df4=df[df3]
df5=df4['Age']<45
df4[df5]

#8
l=[['Product','Category','Price','Promotion'],
   ['Apples','Fruit',1.20,True],['Bananas','Fruit',0.50,False],['Cherries','Fruit',3.0,True],['Dates','Fruit',2.50,True],
   ['ElderBerries','Fruit',4.00,False],['Flour','Bakery',1.50,True],['Grapes','Fruit',2.00,False]]

df=pd.DataFrame(l[1:],columns=l[0])
df1=df.groupby('Category')['Price'].mean()
a=df1['Fruit']
df1=df['Promotion']==False
df2=df[df1]
df3=df2['Price']>a
df2[df3]

#9
l=[['Employee','Department','Manager'],
   ['Alice','Hr','John'],['Bob','IT','Raechel'],['Charlie','Finance','Emily'],['David','IT','Raechel'] ]

m=[['Employee','Project'],['Alice','p1'],['Charlie','p3'],['Eve','p2']]
df=pd.DataFrame(l[1:],columns=l[0])
df
df1=pd.DataFrame(m[1:],columns=m[0])
df1
pd.merge(df,df1,on='Employee',how='left')

#10
data={'Department':['Electronics','Electronics','Clothing','Clothing','Home','Goods'],
      'Salesperson':['Alice','Bob','Charlie','David','Eve',np.NaN],
      'Sales':[70000,50000,30000,40000,60000,np.NaN]
      }
df=pd.DataFrame(data)
df2=df.groupby('Department').agg({'Sales':'mean'})
df2
df2.sort_values(by='Sales',ascending=False)