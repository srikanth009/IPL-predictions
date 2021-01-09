#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:46:51 2020

@author: god
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('/home/god/data/ipl/ipl.csv')
s_df=pd.read_csv('/home/god/data/ipl/matches.csv')

over=[]
for i in range(0,len(df['over_no'].unique())):
    over.append(df[df['over_no']==df['over_no'].unique()[i]])
    
stadium_name=s_df.venue.unique()
stadium=[]
for i in range(len(stadium_name)):
    stadium.append(s_df[s_df.venue==stadium_name[i]])
    
tot=[]
extra=[]
for i in range(len(over)):
    tot.append(over[i]['total_runs_in_ball'].value_counts())
    extra.append(over[i]['extra_runs_ball'].value_counts())

ball=[]
for i in range(len(df['ball_no'].unique())):
    ball.append(df[df['ball_no']==df['ball_no'].unique()[i]])

tot_runs_in_ball=[]
extra_runs_in_ball=[]
for i in range(len(ball)):
    tot_runs_in_ball.append(ball[i]['total_runs_in_ball'].value_counts())
    extra_runs_in_ball.append(ball[i]['extra_runs_ball'].value_counts())

y=[]
yr=[]
for i in range(len(s_df['year'].unique())):

    y.append(s_df[s_df['year']==sorted(s_df['year'].unique())[i]])
    yr.append(df[df['year']==sorted(df['year'].unique())[i]])
    
team=[]
for i in range(len(df['team_batting'].unique())):
    team.append(df[df['team_batting']==df['team_batting'].unique()[i]])
    



t=[]
tb=[]
tf=[]
for i in range(len(y)):
    t.append(y[i][y[i]['winner']==y[i]['toss_winner']])
    tb.append(y[i][y[i]['toss_decision']=='bat'])
    tf.append(y[i][y[i]['toss_decision']=='field'])
    
tbw=[]
tfw=[]
for i in range(len(tb)):
    tbw.append(tb[i][tb[i]['winner']==tb[i]['toss_winner']])
    tfw.append(tf[i][tf[i]['winner']==tf[i]['toss_winner']])



arr=[]
arr1=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
arr6=[]
arr7=[]
arr8=[]
arr9=[]
arr10=[]
arr11=[]
arr12=[]
arr13=[]
arr14=[]
arr15=[]
arr16=[]
arr17=[]
arr18=[]
arr19=[]
arr20=[]
arr21=[]
arr22=[]
arr23=[]
arr24=[]
arr25=[]
arr26=[]
arr27=[]
arr28=[]
arr29=[]
arr30=[]
arr31=[]
arr32=[]
arr33=[]
arr34=[]
arr35=[]
arr36=[]
arr37=[]
arr38=[]
arr39=[]
arr40=[]
arr41=[]
arr42=[]
arr43=[]
arr44=[]
arr45=[]
arr46=[]
arr47=[]
arr48=[]
arr49=[]
arr50=[]
arr81=[]
for i in range(len(t)):
    arr.append((len(t[i])/len(y[i])))
    arr1.append((len(tb[i])/len(y[i])))
    arr2.append((len(tf[i])/len(y[i])))
    arr3.append((len(tbw[i])/len(y[i])))
    arr4.append((len(tbw[i])/len(tb[i])))
    arr5.append((len(tfw[i])/len(y[i])))
    arr6.append((len(tfw[i])/len(tf[i])))
    arr7.append((sum(yr[i]['total_runs_in_ball'])))
    arr9.append(len(y[i][y[i]['wickets']>0])/len(y[i]))
    arr10.append(len(y[i][y[i]['runs']>0])/len(y[i]))
    arr11.append(len(y[i][y[i]['no result']>0])/len(y[i]))
    arr12.append(len(y[i][y[i]['tie']>0])/len(y[i]))
    arr13.append(len(yr[i][yr[i]['total_runs_in_ball']==6])/len(yr[i]))
    arr14.append(len(yr[i][yr[i]['total_runs_in_ball']==6]))
    arr15.append(len(yr[i][(yr[i]['total_runs_in_ball']==4)])/len(yr[i]))
    arr16.append(len(yr[i][yr[i]['total_runs_in_ball']==4]))   
    arr17.append(len(yr[i][yr[i]['total_runs_in_ball']==5])/len(yr[i]))
    arr18.append(len(yr[i][yr[i]['total_runs_in_ball']==5]))
    arr19.append(len(yr[i][(yr[i]['total_runs_in_ball']==7)])/len(yr[i]))
    arr20.append(len(yr[i][yr[i]['total_runs_in_ball']==7])) 
    arr21.append(len(yr[i][(yr[i]['total_runs_in_ball']==0)])/len(yr[i]))
    arr22.append(len(yr[i][yr[i]['total_runs_in_ball']==0])) 
    arr23.append(len(yr[i][(yr[i]['total_runs_in_ball']==1)])/len(yr[i]))
    arr24.append(len(yr[i][yr[i]['total_runs_in_ball']==1])) 
    arr25.append(len(yr[i][(yr[i]['total_runs_in_ball']==2)])/len(yr[i]))
    arr26.append(len(yr[i][yr[i]['total_runs_in_ball']==2])) 
    arr27.append(len(yr[i][(yr[i]['total_runs_in_ball']==3)])/len(yr[i]))
    arr28.append(len(yr[i][yr[i]['total_runs_in_ball']==3])) 
    arr29.append((sum(yr[i]['extra_runs_ball'])))
    arr31.append(len(yr[i][yr[i]['kind'].notnull()]))
    arr32.append(len(yr[i][yr[i]['kind'].notnull()])/len(yr[i]))
    arr33.append(len(yr[i][yr[i]['kind']=='caught']))
    arr34.append(len(yr[i][yr[i]['kind']=='caught'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr35.append(len(yr[i][yr[i]['kind']=='bowled']))
    arr36.append(len(yr[i][yr[i]['kind']=='bowled'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr37.append(len(yr[i][yr[i]['kind']=='run out']))
    arr38.append(len(yr[i][yr[i]['kind']=='run out'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr39.append(len(yr[i][yr[i]['kind']=='lbw']))
    arr40.append(len(yr[i][yr[i]['kind']=='lbw'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr41.append(len(yr[i][yr[i]['kind']=='stumped']))
    arr42.append(len(yr[i][yr[i]['kind']=='stumped'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr43.append(len(yr[i][yr[i]['kind']=='caught and bowled']))
    arr44.append(len(yr[i][yr[i]['kind']=='caught and bowled'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr45.append(len(yr[i][yr[i]['kind']=='retired hurt']))
    arr46.append(len(yr[i][yr[i]['kind']=='retired hurt'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr47.append(len(yr[i][yr[i]['kind']=='hit wicket']))
    arr48.append(len(yr[i][yr[i]['kind']=='hit wicket'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr49.append(len(yr[i][yr[i]['kind']=='obstructing the field']))
    arr50.append(len(yr[i][yr[i]['kind']=='obstructing the field'])/len(yr[i][yr[i]['kind'].notnull()]))
    arr81.append((sum(yr[i]['total_runs_in_ball'])/len(yr[i])))
for i in range(len(t)):
    arr8.append((sum(yr[i]['total_runs_in_ball'])/len(yr[i])))
    arr30.append((sum(yr[i]['extra_runs_ball'])/len(yr[i])))
    



fig = plt.figure()
plt.plot(range(2008,2021),arr)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of winning toss and match')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr1)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of winning toss and select to bat')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr2)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of winning toss and select to bowl')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr3)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('tbw/y')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr4)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('tbw/tb')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr5)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('tfw/y')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr6)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('tfw/tf')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr7)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('total runs in a year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr8)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('total runs in a ball compared to highest year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr9)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('wickets margin matches as proportion per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr10)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs margin matches as proportion per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr11)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('no result per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr12)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('tie per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr13)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of sixes per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr14)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('sixes per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr15)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of fours per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr16)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('fours per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr17)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of fives per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr18)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('fives per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr19)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of seven per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr20)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('seven per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr21)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of zeros per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr22)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('zeros per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr23)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of ones per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr24)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('ones per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr25)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of twos per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr26)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('twos per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr27)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of threes per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr28)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('threes per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr29)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('extras per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr30)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of extras per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr31)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('wickets per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr32)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of wickets per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr33)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('catches per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr34)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of catches per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr35)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('bowled per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr36)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of bowled per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr37)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('run out per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr38)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of run out per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr39)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('lbw per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr40)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of lbw per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr41)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('stumped per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr42)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of stumped per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr43)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('caught and bowled per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr44)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of caught and bowled per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr45)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('retired hurt per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr46)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of retired hurt per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr47)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('hit wicket per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr48)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of hit wicket per year')
plt.show()


fig = plt.figure()
plt.plot(range(2008,2021),arr49)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('obstructing filed per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr50)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('probability of obstructing filed per year')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr81)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs per ball through year')
plt.show()

for i in range(len(over)):
    sns.countplot(over[i]['total_runs_in_ball'])
    plt.show()
    
arr51=[]
arr52=[]
arr53=[]
arr54=[]
arr55=[]
arr55=[]
arr56=[]
arr57=[]
arr58=[]
for i in range(len(over)):
    arr51.append(len(over[i][over[i]['total_runs_in_ball']==0])/len(over[i]))
    arr52.append(len(over[i][over[i]['total_runs_in_ball']==1])/len(over[i]))
    arr53.append(len(over[i][over[i]['total_runs_in_ball']==2])/len(over[i]))
    arr54.append(len(over[i][over[i]['total_runs_in_ball']==3])/len(over[i]))
    arr55.append(len(over[i][over[i]['total_runs_in_ball']==4])/len(over[i]))
    arr56.append(len(over[i][over[i]['total_runs_in_ball']==5])/len(over[i]))
    arr57.append(len(over[i][over[i]['total_runs_in_ball']==6])/len(over[i]))
    arr58.append(len(over[i][over[i]['total_runs_in_ball']==7])/len(over[i]))

    
fig = plt.figure()
plt.plot(range(len(over)),arr51)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of zero runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr52)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of one runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr53)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of two runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr54)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of three runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr55)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of four runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr56)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of five runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr57)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of six runs in ball through over')
plt.show()

fig = plt.figure()
plt.plot(range(len(over)),arr58)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of seven runs in ball through over')
plt.show()

arr59=[]
for i in range(len(over)):
    arr59.append(sum(over[i]['total_runs_in_ball'])/len(over[i]))
    
fig = plt.figure()
plt.plot(range(len(over)),arr59)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('average runs in ball through overs')
plt.show()

arr60=[]
arr61=[]
arr62=[]
arr63=[]
arr64=[]
arr65=[]
arr66=[]
arr67=[]
arr68=[]
arr69=[]
arr70=[]
arr71=[]
arr72=[]
arr73=[]
arr74=[]
arr75=[]
arr76=[]
arr77=[]
arr78=[]
arr79=[]
arr80=[]
for i in range(len(yr)):
    arr60.append(sum(yr[i][yr[i]['over_no']==0]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==0]))
    arr61.append(sum(yr[i][yr[i]['over_no']==1]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==1]))
    arr62.append(sum(yr[i][yr[i]['over_no']==2]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==2]))
    arr63.append(sum(yr[i][yr[i]['over_no']==3]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==3]))
    arr64.append(sum(yr[i][yr[i]['over_no']==4]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==4]))
    arr65.append(sum(yr[i][yr[i]['over_no']==5]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==5]))
    arr66.append(sum(yr[i][yr[i]['over_no']==6]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==6]))
    arr67.append(sum(yr[i][yr[i]['over_no']==7]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==7]))
    arr68.append(sum(yr[i][yr[i]['over_no']==8]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==8]))
    arr69.append(sum(yr[i][yr[i]['over_no']==9]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==9]))
    arr70.append(sum(yr[i][yr[i]['over_no']==10]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==10]))
    arr71.append(sum(yr[i][yr[i]['over_no']==11]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==11]))
    arr72.append(sum(yr[i][yr[i]['over_no']==12]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==12]))
    arr73.append(sum(yr[i][yr[i]['over_no']==13]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==13]))
    arr74.append(sum(yr[i][yr[i]['over_no']==14]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==14]))
    arr75.append(sum(yr[i][yr[i]['over_no']==15]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==15]))
    arr76.append(sum(yr[i][yr[i]['over_no']==16]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==16]))
    arr77.append(sum(yr[i][yr[i]['over_no']==17]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==17]))
    arr78.append(sum(yr[i][yr[i]['over_no']==18]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==18]))
    arr79.append(sum(yr[i][yr[i]['over_no']==19]['total_runs_in_ball'])/len(yr[i][yr[i]['over_no']==19]))

        
fig = plt.figure()
plt.plot(range(2008,2021),arr60)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in zero over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr61)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in first over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr62)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in second over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr63)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in third over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr64)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in fourth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr65)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in fifth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr66)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in sixth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr67)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in seventh over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr68)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in eighth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr69)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in ninth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr70)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in tenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr71)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in eleventh over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr72)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in twelth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr73)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in thirteenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr74)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in fourteenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr75)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in fiftenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr76)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in sixteenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr77)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in seventeenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr78)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in eighteenth over per ball through years')
plt.show()

fig = plt.figure()
plt.plot(range(2008,2021),arr79)
ax = fig.gca()
ax.set_xticks(range(2008,2021))
ax.grid()
plt.xlabel('year------->')
plt.ylabel('runs in ninteenth over per ball through years')
plt.show()

for i in range(len(over)):
    arr80.append((len(over[i][over[i]['kind'].notnull()])/len(over[i])))
    
fig = plt.figure()
plt.plot(range(len(over)),arr80)
plt.plot(range(len(over)),arr59)
ax = fig.gca()
ax.set_xticks(range(len(over)))
ax.grid()
plt.xlabel('over------->')
plt.ylabel('probability of wicket per ball through over')
plt.show()   

fig = plt.figure()
plt.scatter(arr59,arr80)
ax = fig.gca()
ax.grid()
plt.xlabel('runs------->')
plt.ylabel('wickets------>')
plt.show()   

fig = plt.figure()
plt.scatter(arr51,arr52)
ax = fig.gca()
ax.grid()
plt.xlabel('zeros------->')
plt.ylabel('ones------>')
plt.show()   

fig = plt.figure()
plt.scatter(arr51,arr57)
ax = fig.gca()
ax.grid()
plt.xlabel('zeros------->')
plt.ylabel('sixes------>')
plt.show() 

fig = plt.figure()
plt.scatter(arr51,arr80)
ax = fig.gca()
ax.grid()
plt.xlabel('zeros------->')
plt.ylabel('wickets------>')
plt.show() 

fig = plt.figure()
plt.scatter(arr51,arr59)
ax = fig.gca()
ax.grid()
plt.xlabel('zeros------->')
plt.ylabel('runs------>')
plt.show() 

fig = plt.figure()
plt.scatter(arr57,arr80)
ax = fig.gca()
ax.grid()
plt.ylabel('wickets------->')
plt.xlabel('sixes------>')
plt.show()  

fig = plt.figure()
plt.scatter(arr80,arr55)
ax = fig.gca()
ax.grid()
plt.xlabel('wickets------->')
plt.ylabel('fours------>')
plt.show()  

fig = plt.figure()
plt.scatter(arr59,arr57)
ax = fig.gca()
ax.grid()
plt.xlabel('runs------->')
plt.ylabel('sixes------>')
plt.show()  

fig = plt.figure()
plt.scatter(arr59,arr51)
ax = fig.gca()
ax.grid()
plt.xlabel('runs------->')
plt.ylabel('zeros------>')
plt.show()  

fig = plt.figure()
plt.scatter(arr59,arr55)
ax = fig.gca()
ax.grid()
plt.xlabel('runs------->')
plt.ylabel('fours------>')
plt.show()  

fig = plt.figure()
plt.scatter(arr59,arr52)
ax = fig.gca()
ax.grid()
plt.xlabel('runs------->')
plt.ylabel('ones------>')
plt.show()  




for i in range(len(df['match_no'].unique())):
    k=df[df['match_no']==df['match_no'].unique()[i]]
    k.to_csv('/home/god/data/ipl/matchwise/{}.csv'.format(df['match_no'].unique()[i]))       
    

for i in range(len(df['year'].unique())):
    k=df[df['year']==df['year'].unique()[i]]
    k.to_csv('/home/god/data/ipl/yearwise/{}.csv'.format(df['year'].unique()[i]))
    
for i in range(len(df['batsman'].unique())):
    k=df[df['batsman']==df['batsman'].unique()[i]]
    k.to_csv('/home/god/data/ipl/batsman_profile/{}.csv'.format(df['batsman'].unique()[i]))

for i in range(len(df['bowler'].unique())):
    k=df[df['bowler']==df['bowler'].unique()[i]]
    k.to_csv('/home/god/data/ipl/bowler_profile/{}.csv'.format(df['bowler'].unique()[i]))

s_df['city'].fillna('Dubai',inplace=True)   
s_df['city'].replace({'Bangalore':'Bengaluru'},inplace=True)  
for i in range(len(s_df['city'].unique())):
    k1=[]
    k=s_df[s_df['city']==s_df['city'].unique()[i]]
    for j in range(len(k['Match_no'].unique())):
        k1.append(pd.read_csv('/home/god/data/ipl/matchwise/{}.csv'.format(k['Match_no'].unique()[j]-1)))
    k2=pd.concat(k1,axis=0)
    k2.to_csv('/home/god/data/ipl/venue/{}.csv'.format(s_df['city'].unique()[i]))    
    
    
s_df.columns
k=s_df[s_df['city'].isnull()]
