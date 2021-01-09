#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:03:42 2020

@author: god
"""


import glob
import pandas as pd
import matplotlib.pyplot as plt
g=sorted(glob.glob('/home/god/data/ipl/venue/*.csv'))


venue=[]
runs_in_venue=[]
wickets_in_venue=[]
for i in range(len(g)):
    venue.append(g[i].split('/')[6])
    runs_in_venue.append(sum(pd.read_csv(g[i])['total_runs_in_ball'])/len(pd.read_csv(g[i])['total_runs_in_ball'])*120)
    wickets_in_venue.append(len(pd.read_csv(g[i])[pd.read_csv(g[i])['kind'].notnull()])/len(pd.read_csv(g[i]))*120)
    
fig=plt.figure()
plt.scatter(runs_in_venue,wickets_in_venue)
plt.xlabel('runs in innings')
plt.ylabel('wickets')
plt.suptitle('venue', fontsize=14, fontweight='bold')
ax = fig.gca()
for i in range(len(venue)):
    ax.annotate(i, (runs_in_venue[i], wickets_in_venue[i]))
ax.grid()
plt.show()


for i in range(len(g)):
    df=pd.read_csv(g[i])
    runs=[]
    wickets=[]
    for j in range(len(df['year'].unique())):
        k=df[df['year']==df['year'].unique()[j]]
        runs.append((sum(k['total_runs_in_ball'])/len(k))*120)
        wickets.append((len(k[k['kind'].notnull()])/len(k['kind']))*120)
    fig=plt.figure()
    plt.scatter(runs,wickets)
    plt.xlabel('runs in innings')
    plt.ylabel('wickets')
    plt.suptitle('{}'.format(g[i].split('/')[6]))
    ax = fig.gca()
    for k in range(len(df['year'].unique())):
        ax.annotate(df['year'].unique()[k], (runs[k], wickets[k]))
    ax.grid()
    plt.show()
        
        

