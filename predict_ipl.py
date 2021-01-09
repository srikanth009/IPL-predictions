#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:10:56 2020

@author: god
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso, Ridge 
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score 
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize

df=pd.read_csv('/home/god/data/ipl/predict.csv')

df_train=df[df['year']<=2016]
df_test=df[df['year']>2016]

X=df_train[['day','month','year','wickets in 1 to 6 1st innings',
            'venue average runs in 1st innings','venue average wickets in 1st innings']]
y=df_train[['runs in 7 to 14 overs 1st innings']]


X1=df_test[['day','month','year','wickets in 1 to 6 1st innings',
            'venue average runs in 1st innings','venue average wickets in 1st innings']]


y1=df_test[['runs in 7 to 14 overs 1st innings']]





X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

lr = LinearRegression()
lasso = Lasso() 
ridge = Ridge() 
dtr = DecisionTreeRegressor() 
rfr = RandomForestRegressor(n_estimators=50) 


lr.fit(X_train, y_train) 
lasso.fit(X_train, y_train) 
ridge.fit(X_train, y_train) 
dtr.fit(X_train, y_train) 
rfr.fit(X_train, y_train) 


y_pred_lr = lr.predict(X_test) 
y_pred_lasso = lasso.predict(X_test) 
y_pred_ridge = ridge.predict(X_test) 
y_pred_dtr = dtr.predict(X_test)
y_pred_rfr = rfr.predict(X_test)







pred=lasso.predict(df[['day','month','year','wickets in 1 to 6 1st innings',
            'venue average runs in 1st innings','venue average wickets in 1st innings']])
act=df[['runs in 7 to 14 overs 1st innings']]

dif=[]
for i in range(len(pred)):
    k=((abs(pred[i]-act['runs in 7 to 14 overs 1st innings'].iloc[i]))/act['runs in 7 to 14 overs 1st innings'].iloc[i])
    dif.append(k*100)    

pred1=pred 
dif1=dif

count=0
count1=0
count2=0
for i in range(len(dif)):
    if dif[i]<=10:
        count+=1
    elif dif[i]<=20:
        count1+=1
    elif dif[i]<=30:
        count2+=1
print('lasso',count/816,count1/816,count2/816,(count+count1+count2)/816)




plt.scatter(pred,act['runs in 7 to 14 overs 1st innings'])
plt.xlabel('pred')
plt.ylabel('act')
plt.xticks(range(0,150,10))
plt.show()

plt.scatter(dif,act['runs in 7 to 14 overs 1st innings'])
plt.xlabel('dif')
plt.ylabel('act')
plt.show()




def r_squared(a,p,x0,x1):
    m=np.mean(a)
    s=[]
    for i in range(len(p)):
        d=p[i]-m
        d=d**2
        s.append(d)
    ssr=sum(s)
    s=[]
    for i in range(len(p)):
        d=p[i]-a.iloc[i]
        d=d**2
        s.append(d)
    sse=sum(s)
    s=[]
    for i in range(len(p)):
        d=m-a.iloc[i]
        d=d**2
        s.append(d)
    sst=sum(s)
    r_sqr = 1-((sse*(x0-1))/(sst*(x0-x1-1)))
    return r_sqr
    
        

print(r_squared(act['runs in 7 to 14 overs 1st innings'],pred,df.shape[0],df.shape[1]))

print(r_squared(y['runs in 7 to 14 overs 1st innings'],lasso.predict(X),X.shape[0],X.shape[1]))

print(r_squared(y1['runs in 7 to 14 overs 1st innings'],lasso.predict(X1),X1.shape[0],X1.shape[1]))

pred=lr.predict(df[['day','month','year','wickets in 1 to 6 1st innings',
            'venue average runs in 1st innings','venue average wickets in 1st innings']])

dif=[]
for i in range(len(pred)):
    k=((abs(pred[i]-act['runs in 7 to 14 overs 1st innings'].iloc[i]))/act['runs in 7 to 14 overs 1st innings'].iloc[i])
    dif.append(k[0]*100)    


count=0
count1=0
count2=0
for i in range(len(dif)):
    if dif[i]<=10:
        count+=1
    elif dif[i]<=20:
        count1+=1
    elif dif[i]<=30:
        count2+=1
print('linear',count/816,count1/816,count2/816,(count+count1+count2)/816)



df['dif']=dif
df['dif1']=dif1
df['pred1']=pred1
df['pred']=pred

plt.scatter(pred,act['runs in 7 to 14 overs 1st innings'])
plt.xlabel('pred')
plt.ylabel('actual')
plt.show()

plt.scatter(dif,act['runs in 7 to 14 overs 1st innings'])
plt.xlabel('dif')
plt.ylabel('act')
plt.show()

fig=plt.figure()
sns.boxplot(df['month'],df['dif'])
ax = fig.gca()
ax.grid()
plt.show()


fig=plt.figure()
sns.boxplot(df['month'],dif1)
ax = fig.gca()
ax.grid()
plt.show()

sns.boxplot(df['year'],dif)
plt.show()

sns.boxplot(df['year'],dif1)
plt.show()

plt.scatter(dif,dif1)
plt.xlabel('dif')
plt.ylabel('dif1')
plt.show()

plt.scatter(pred,pred1)
plt.xlabel('pred')
plt.ylabel('pred1')
plt.show()

print(r_squared(act['runs in 7 to 14 overs 1st innings'],pred,df.shape[0],X.shape[1]))

print(r_squared(y['runs in 7 to 14 overs 1st innings'],lr.predict(X),X.shape[0],X.shape[1]))

print(r_squared(y1['runs in 7 to 14 overs 1st innings'],lr.predict(X1),X1.shape[0],X1.shape[1]))


df['dif']=dif
df['dif1']=dif1
df['pred1']=pred1
df['pred']=pred

sns.boxplot(df['dif'])
plt.show()

sns.boxplot(df['dif1'])
plt.show()