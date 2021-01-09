#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:55:06 2020

@author: god
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

s_df=pd.read_csv('/home/god/data/ipl/matches.csv')
s_df['city'].fillna('Dubai',inplace=True)   
s_df['city'].replace({'Bangalore':'Bengaluru'},inplace=True)  


six_overs_runs=[]
seven_fourteen_runs=[]
fifteen_20_runs=[]
total_runs_in_ball=[]
six_overs_wickets=[]
seven_fourteen_wickets=[]
fifteen_20_wickets=[]
total_wickets=[]
first_inn_win=[]
toss_winner=[]
balls_in_inn=[]
balls_in_six=[]
balls_in_fourteen=[]
balls_in_twenty=[]
for j in range(0,len(s_df)):
    df=pd.read_csv('/home/god/data/ipl/matchwise/{}.csv'.format(j))
    df=df[df['innings']==1]
    six_overs_runs.append(sum(df[df['over_no']<=5]['total_runs_in_ball']))
    seven_fourteen_runs.append(sum(df[(df['over_no']>=6)&(df['over_no']<=13)]['total_runs_in_ball']))
    fifteen_20_runs.append(sum(df[df['over_no']>=14]['total_runs_in_ball']))
    total_runs_in_ball.append(sum(df['total_runs_in_ball']))
    balls_in_inn.append(len(df))
    balls_in_six.append(len(df[df['over_no']<=5]['total_runs_in_ball']))
    balls_in_fourteen.append(len(df[(df['over_no']>=6)&(df['over_no']<=13)]['total_runs_in_ball']))
    balls_in_twenty.append(len(df[df['over_no']>=14]['total_runs_in_ball']))
    if s_df['winner'][j]==df['team_batting'].iloc[0]:
        first_inn_win.append(1)
    else:
        first_inn_win.append(0)
    if s_df['toss_winner'][j]==df['team_batting'].iloc[0]:
        toss_winner.append(1)
    else:
        toss_winner.append(0)
    df=df[df['kind'].notnull()]
    six_overs_wickets.append(len(df[df['over_no']<=5]))
    seven_fourteen_wickets.append(len(df[(df['over_no']>=6)&(df['over_no']<=13)]))
    fifteen_20_wickets.append(len(df[df['over_no']>=14]))
    total_wickets.append(len(df))
 
six_overs_runs1=[]
seven_fourteen_runs1=[]
fifteen_20_runs1=[]
total_runs_in_ball1=[]
six_overs_wickets1=[]
seven_fourteen_wickets1=[]
fifteen_20_wickets1=[]
total_wickets1=[]
balls_in_inn1=[]
balls_in_six1=[]
balls_in_fourteen1=[]
balls_in_twenty1=[]
for j in range(0,len(s_df)):
    df=pd.read_csv('/home/god/data/ipl/matchwise/{}.csv'.format(j))
    df=df[df['innings']==2]
    six_overs_runs1.append(sum(df[df['over_no']<=5]['total_runs_in_ball']))
    seven_fourteen_runs1.append(sum(df[(df['over_no']>=6)&(df['over_no']<=13)]['total_runs_in_ball']))
    fifteen_20_runs1.append(sum(df[df['over_no']>=14]['total_runs_in_ball']))
    total_runs_in_ball1.append(sum(df['total_runs_in_ball']))
    balls_in_inn1.append(len(df))
    balls_in_six1.append(len(df[df['over_no']<=5]['total_runs_in_ball']))
    balls_in_fourteen1.append(len(df[(df['over_no']>=6)&(df['over_no']<=13)]['total_runs_in_ball']))
    balls_in_twenty1.append(len(df[df['over_no']>=14]['total_runs_in_ball']))
    df=df[df['kind'].notnull()]
    six_overs_wickets1.append(len(df[df['over_no']<=5]))
    seven_fourteen_wickets1.append(len(df[(df['over_no']>=6)&(df['over_no']<=13)]))
    fifteen_20_wickets1.append(len(df[df['over_no']>=14]))
    total_wickets1.append(len(df))

d1=dict()
d1['D/L']=1
s_df['method']=s_df['method'].map(d1)
d=dict()
d['match_no']=s_df['Match_no']
d['day']=s_df['day']
d['month']=s_df['month']
d['year']=s_df['year']
d['city']=s_df['city']
d['toss_winner']=toss_winner
d['runs in 1 to 6 overs 1st innings']=six_overs_runs
d['runs in 7 to 14 overs 1st innings']=seven_fourteen_runs
d['runs in 15 to 20 overs 1st innings']=fifteen_20_runs
d['total runs in 1st innings']=total_runs_in_ball
d['wickets in 1 to 6 1st innings']=six_overs_wickets
d['wickets in 7 to 14 overs 1st innings']=seven_fourteen_wickets
d['wickets in 15 to 20 overs 1st innings']=fifteen_20_wickets
d['total wickets in 1st innings']=total_wickets
d['runs in 1 to 6 overs 2nd innings']=six_overs_runs1
d['runs in 7 to 14 overs 2nd innings']=seven_fourteen_runs1
d['runs in 15 to 20 overs 2nd innings']=fifteen_20_runs1
d['total runs in 2nd innings']=total_runs_in_ball1
d['wickets in 1 to 6 2nd innings']=six_overs_wickets1
d['wickets in 7 to 14 overs 2nd innings']=seven_fourteen_wickets1
d['wickets in 15 to 20 overs 2nd innings']=fifteen_20_wickets1
d['total wickets in 2nd innings']=total_wickets1
d['balls in 1st innings']=balls_in_inn
d['balls in 2nd innings']=balls_in_inn1
d['method']=s_df['method']
d['target']=first_inn_win
df=pd.DataFrame(d)

    


df['method'].fillna(0,inplace=True)
d1=dict()
venue_runs=[]
venue_wickets=[]
venue_runs1=[]
venue_wickets1=[]
for i in range(len(s_df)):
    if s_df['city'].iloc[i] in d1:
        k=df[df['city']==df['city'].iloc[i]]
        k=df[df['match_no']<i+1]
        venue_runs.append((sum(k['total runs in 1st innings'])/sum(k['balls in 1st innings']))*120)
        venue_runs1.append((sum(k['total runs in 2nd innings'])/sum(k['balls in 2nd innings']))*120)
        venue_wickets.append((sum(k['total wickets in 1st innings'])/sum(k['balls in 1st innings']))*120)
        venue_wickets1.append((sum(k['total wickets in 2nd innings'])/sum(k['balls in 2nd innings']))*120)
    else:
        d1[df['city'].iloc[i]]=1
        venue_runs.append(0)
        venue_runs1.append(0)
        venue_wickets.append(0)
        venue_wickets1.append(0)

d=dict()
d['match_no']=s_df['Match_no']
d['day']=s_df['day']
d['month']=s_df['month']
d['year']=s_df['year']
d['toss_winner']=toss_winner
d['venue average runs in 1st innings']=venue_runs
d['venue average runs in 2nd innings']=venue_runs1
d['venue average wickets in 1st innings']=venue_wickets
d['venue average wickets in 2nd innings']=venue_wickets1
d['runs in 1 to 6 overs 1st innings']=six_overs_runs
d['number of balls in six overs 1st innings']=balls_in_six
d['runs in 7 to 14 overs 1st innings']=seven_fourteen_runs
d['number of balls in fourteen overs 1st innings']=balls_in_fourteen
d['runs in 15 to 20 overs 1st innings']=fifteen_20_runs
d['number of balls in twenty overs 1st innings']=balls_in_twenty
d['total runs in 1st innings']=total_runs_in_ball
d['balls in 1st innings']=balls_in_inn
d['wickets in 1 to 6 1st innings']=six_overs_wickets
d['wickets in 7 to 14 overs 1st innings']=seven_fourteen_wickets
d['wickets in 15 to 20 overs 1st innings']=fifteen_20_wickets
d['total wickets in 1st innings']=total_wickets
d['runs in 1 to 6 overs 2nd innings']=six_overs_runs1
d['number of balls in six overs 2nd innings']=balls_in_six1
d['runs in 7 to 14 overs 2nd innings']=seven_fourteen_runs1
d['number of balls in six overs 2nd innings']=balls_in_fourteen1
d['runs in 15 to 20 overs 2nd innings']=fifteen_20_runs1
d['number of balls in twenty overs 2nd innings']=balls_in_twenty1
d['total runs in 2nd innings']=total_runs_in_ball1
d['balls in 2nd innings']=balls_in_inn1
d['wickets in 1 to 6 2nd innings']=six_overs_wickets1
d['wickets in 7 to 14 overs 2nd innings']=seven_fourteen_wickets1
d['wickets in 15 to 20 overs 2nd innings']=fifteen_20_wickets1
d['total wickets in 2nd innings']=total_wickets1
d['method']=s_df['method']
d['target']=first_inn_win
df=pd.DataFrame(d)
df['method'].fillna(0,inplace=True)
df.to_csv('/home/god/data/ipl/predict.csv')

fig = plt.figure()
plt.scatter(df['year'],total_runs_in_ball)
plt.xlabel('year')
plt.ylabel('total runs')
plt.suptitle(str(df['year'].iloc[0])+' first innings', fontsize=14, fontweight='bold')
ax = fig.gca()
ax.grid()
plt.show()
for i in range(len(df['year'].unique())):
    k=df[df['year']==df['year'].unique()[i]]
    fig = plt.figure()
    sns.boxplot(k['target'],k['total runs in 1st innings'])
    plt.xlabel('year')
    plt.ylabel('total runs')
    plt.suptitle('first innings win {}'.format(df['year'].unique()[i]), fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    ax.set_yticks(range(40,280,20))
    plt.show()

fig = plt.figure()
plt.scatter(df['target'],df['total runs in 1st innings'])
plt.xlabel('year')
plt.ylabel('total runs')
plt.suptitle('first innings win', fontsize=14, fontweight='bold')
ax = fig.gca()
ax.grid()
plt.show()

