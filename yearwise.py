#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:02:16 2020

@author: god
"""


import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
g=sorted(glob.glob('/home/god/data/ipl/yearwise/*.csv'))
for i in range(len(g)):
    six_overs_runs=[]
    seven_fourteen_runs=[]
    fifteen_20_runs=[]
    total_runs_in_ball=[]
    df=pd.read_csv(g[i])
    for j in range(len(df['match_no'].unique())):
        df=pd.read_csv(g[i])
        df=df[df['match_no']==df['match_no'].unique()[j]]
        df=df[df['innings']==1]
        six_overs_runs.append(sum(df[df['over_no']<=5]['total_runs_in_ball']))
        seven_fourteen_runs.append(sum(df[(df['over_no']>=6)&(df['over_no']<=13)]['total_runs_in_ball']))
        fifteen_20_runs.append(sum(df[df['over_no']>=14]['total_runs_in_ball']))
        total_runs_in_ball.append(sum(df['total_runs_in_ball']))
        
    six_overs_runs1=[]
    seven_fourteen_runs1=[]
    fifteen_20_runs1=[]
    total_runs_in_ball1=[]
    df=pd.read_csv(g[i])
    for j in range(len(df['match_no'].unique())):
        df=pd.read_csv(g[i])
        df=df[df['match_no']==df['match_no'].unique()[j]]
        df=df[df['innings']==2]
        six_overs_runs1.append(sum(df[df['over_no']<=5]['total_runs_in_ball']))
        seven_fourteen_runs1.append(sum(df[(df['over_no']>=6)&(df['over_no']<=13)]['total_runs_in_ball']))
        fifteen_20_runs1.append(sum(df[df['over_no']>=14]['total_runs_in_ball']))
        total_runs_in_ball1.append(sum(df['total_runs_in_ball']))
     
        
    fig = plt.figure()
    plt.scatter(six_overs_runs,total_runs_in_ball)
    plt.xlabel('0 to 6 overs')
    plt.ylabel('total runs')
    plt.suptitle(str(df['year'].iloc[0])+' first innings', fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    plt.show()
    
    
    fig = plt.figure()
    plt.scatter(six_overs_runs1,total_runs_in_ball1)
    plt.xlabel('0 to 6 overs')
    plt.ylabel('total runs')
    plt.suptitle(str(df['year'].iloc[0])+' second innings', fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    plt.show()
    
    
    fig = plt.figure()
    plt.scatter(seven_fourteen_runs,total_runs_in_ball)
    plt.xlabel('7 to 14 overs')
    plt.ylabel('total runs')
    plt.suptitle(str(df['year'].iloc[0])+' first innings', fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    plt.show()
    
    
    fig = plt.figure()
    plt.scatter(seven_fourteen_runs1,total_runs_in_ball1)
    plt.xlabel('7 to 14 overs')
    plt.ylabel('total runs')
    plt.suptitle(str(df['year'].iloc[0])+' second innings', fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    plt.show()
    
    fig = plt.figure()
    plt.scatter(fifteen_20_runs,total_runs_in_ball)
    plt.xlabel('15 to 20 overs')
    plt.ylabel('total runs')
    plt.suptitle(str(df['year'].iloc[0])+' first innings', fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    plt.show()
    
    
    fig = plt.figure()
    plt.scatter(fifteen_20_runs1,total_runs_in_ball1)
    plt.xlabel('15 to 20 overs')
    plt.ylabel('total runs')
    plt.suptitle(str(df['year'].iloc[0])+' second innings', fontsize=14, fontweight='bold')
    ax = fig.gca()
    ax.grid()
    plt.show()
    
    
    
