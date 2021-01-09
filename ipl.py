#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:59:55 2020

@author: god
"""

import glob
import os
from zipfile import ZipFile
import yaml
import numpy as np
import datetime
import pandas as pd
os.system('rm /home/god/data/ipl/*.yaml')
os.system("curl https://cricsheet.org/downloads/ipl.zip --output /home/god/data/ipl.zip")


with ZipFile('/home/god/data/ipl.zip', 'r') as zipObj:
   zipObj.extractall('/home/god/data/ipl')

files = glob.glob("/home/god/data/ipl/*.yaml")


c=[]
for i in range(0,len(files)):
    with open(files[i]) as file:
        doc=yaml.load(file)
        c.append(doc)
        

dates=[]
for i in range(len(c)):
    if type(c[i]['info']['dates'][0])==str:
      c[i]['info']['dates'][0]=datetime.datetime.strptime(c[i]['info']['dates'][0], '%Y-%m-%d').date()  
    dates.append(c[i]['info']['dates'][0])




v=[x for _,x in sorted(zip(dates,files))]
for i in range(len(v)):
    os.system('mv'+' '+v[i]+' '+'/home/god/data/ipl/{}.yaml'.format(i+1))
            
            
files = glob.glob("/home/god/data/ipl/*.yaml")


c=[]
for i in range(0,len(files) ):
    with open("/home/god/data/ipl/{}.yaml".format(i+1)) as file:
        doc=yaml.load(file)
        c.append(doc)

dates=[]
man_of_match=[]
city=[]
umpire1=[]
umpire2=[]
venue=[]
toss_decision=[]
toss_winner=[]
team1=[]
team2=[]
runs=[]
wickets=[]
eliminator=[]
method=[]
result=[]
winner=[]

for i in range(len(c)):
    if type(c[i]['info']['dates'][0])==str:
      c[i]['info']['dates'][0]=datetime.datetime.strptime(c[i]['info']['dates'][0], '%Y-%m-%d').date()  
    dates.append(c[i]['info']['dates'][0])
    if 'player_of_match' in c[i]['info']:
        man_of_match.append(c[i]['info']['player_of_match'][0])
    else:
        man_of_match.append(None)
    if 'city' in c[i]['info']:
        city.append(c[i]['info']['city'])
    else:
        city.append(None)
    venue.append(c[i]['info']['venue'])
    umpire1.append(c[i]['info']['umpires'][0])
    umpire2.append(c[i]['info']['umpires'][1])
    toss_decision.append(c[i]['info']['toss']['decision'])
    toss_winner.append(c[i]['info']['toss']['winner'])
    team1.append(c[i]['info']['teams'][0])
    team2.append(c[i]['info']['teams'][1])
    if 'by' in c[i]['info']['outcome']:
        if 'runs' in c[i]['info']['outcome']['by']:
            runs.append(c[i]['info']['outcome']['by']['runs'])
            wickets.append(None)
        elif 'wickets' in c[i]['info']['outcome']['by']:
            wickets.append(c[i]['info']['outcome']['by']['wickets'])
            runs.append(None)
    else:
        runs.append(None)
        wickets.append(None)
    if 'eliminator' in c[i]['info']['outcome']:
        eliminator.append(1)
    else:
        eliminator.append(0)
    if 'method' in c[i]['info']['outcome']:
        method.append(c[i]['info']['outcome']['method'])
    else:
        method.append(None)
    if 'result' in c[i]['info']['outcome']:
        result.append(c[i]['info']['outcome']['result'])
        
    else:
        result.append(None)
    if 'winner' in c[i]['info']['outcome']:
        winner.append(c[i]['info']['outcome']['winner'])
    elif 'eliminator' in c[i]['info']['outcome']:
        winner.append(c[i]['info']['outcome']['eliminator'])
    else:
        winner.append(None)        
    
    
tie=[]
no_result=[]
for i in range(len(result)):
    if result[i]=='tie':
        tie.append(1)
        no_result.append(0)
    elif result[i]=='no result':
        no_result.append(1)
        tie.append(0)
    else:
        no_result.append(0)
        tie.append(0)
day=[]
month=[]
year=[]
for i in range(len(dates)):
    day.append(int(dates[i].strftime('%Y-%m-%d').split('-')[2]))
    month.append(int(dates[i].strftime('%Y-%m-%d').split('-')[1]))
    year.append(int(dates[i].strftime('%Y-%m-%d').split('-')[0]))
    


d=dict()
d['Match_no']=range(1,len(day)+1)
d['day']=day
d['month']=month
d['year']=year
d['date']=dates
d['venue']=venue
d['city']=city
d['umpire1']=umpire1
d['umpire2']=umpire2
d['team1']=team1
d['team2']=team2
d['toss_winner']=toss_winner
d['toss_decision']=toss_decision
d['eliminator']=eliminator
d['method']=method
d['tie']=tie
d['no result']=no_result
d['winner']=winner
d['runs']=runs
d['wickets']=wickets
d['man_of_the_match']=man_of_match

df=pd.DataFrame(d)

df.to_csv('/home/god/data/ipl/matches.csv')



bb=[]
tp=[]
innings=[]
match=[]
city=[]
team1=[]
team2=[]
man=[]
outcome=[]
winner=[]
dates=[]
venue=[]
for i in range(len(c)):
    for j in range(len(c[i]['innings'])):
        if '1st innings' in c[i]['innings'][j]:
            for k in range(len(c[i]['innings'][j]['1st innings']['deliveries'])):
                bb.append(c[i]['innings'][j]['1st innings']['deliveries'][k])
                tp.append(c[i]['innings'][j]['1st innings']['team'])
                innings.append(1)
                match.append(i)
                team1.append(c[i]['info']['teams'][0])
                team2.append(c[i]['info']['teams'][1])
                if 'city' in c[i]['info']:
                    city.append(c[i]['info']['city'])
                else:
                    city.append('neutral')
                if 'player_of_match' in c[i]['info']:
                    man.append(c[i]['info']['player_of_match'][0])
                else:
                    man.append(None)


                if 'by' in c[i]['info']['outcome']:
                    outcome.append(c[i]['info']['outcome']['by'])
                elif 'result' in c[i]['info']['outcome']:
                    outcome.append(c[i]['info']['outcome']['result'])
                if 'winner' in c[i]['info']['outcome']:
                    winner.append(c[i]['info']['outcome']['winner'])
                elif 'eliminator' in c[i]['info']['outcome']:
                    winner.append(c[i]['info']['outcome']['eliminator'])
                else:
                    winner.append('no_result')

                dates.append(c[i]['info']['dates'][0])
                if 'venue' in c[i]['info']: 
                    venue.append("".join(c[i]['info']['venue']))
                else:
                    venue.append(None)
        elif '2nd innings' in c[i]['innings'][j]:
            for k in range(len(c[i]['innings'][j]['2nd innings']['deliveries'])):
                bb.append(c[i]['innings'][j]['2nd innings']['deliveries'][k])
                tp.append(c[i]['innings'][j]['2nd innings']['team'])
                innings.append(2)
                match.append(i)
                team1.append(c[i]['info']['teams'][0])
                team2.append(c[i]['info']['teams'][1])
                if 'city' in c[i]['info']:
                    city.append(c[i]['info']['city'])
                else:
                    city.append('neutral')
                if 'player_of_match' in c[i]['info']:
                    man.append(c[i]['info']['player_of_match'][0])
                else:
                    man.append(None)
                if 'by' in c[i]['info']['outcome']:
                    outcome.append(c[i]['info']['outcome']['by'])
                elif 'result' in c[i]['info']['outcome']:
                    outcome.append(c[i]['info']['outcome']['result'])
                if 'winner' in c[i]['info']['outcome']:
                    winner.append(c[i]['info']['outcome']['winner'])
                elif 'eliminator' in c[i]['info']['outcome']:
                    winner.append(c[i]['info']['outcome']['eliminator'])
                else:
                    winner.append('no_result')

                dates.append(c[i]['info']['dates'][0])
                if 'venue' in c[i]['info']: 
                    venue.append("".join(c[i]['info']['venue']))
                else:
                    venue.append(None)




batsman=[]
bowler=[]
non_striker=[]
rs=[]
w=[]
extras=[]
replacements=[]
ball_no=[]
for i in range(len(bb)):
    ball_no.append(list(bb[i].keys())[0])
    if 'batsman' in bb[i][list(bb[i].keys())[0]]:
        batsman.append(bb[i][list(bb[i].keys())[0]]['batsman'])
    else:
        batsman.append(None)
    if 'bowler' in bb[i][list(bb[i].keys())[0]]:
        bowler.append(bb[i][list(bb[i].keys())[0]]['bowler'])
    else:
        bowler.append(None)
    if 'non_striker' in bb[i][list(bb[i].keys())[0]]:
        non_striker.append(bb[i][list(bb[i].keys())[0]]['non_striker'])
    else:
        non_striker.append(None)
    if 'runs' in bb[i][list(bb[i].keys())[0]]:
        rs.append(bb[i][list(bb[i].keys())[0]]['runs'])
    else:
        rs.append(None)
    if 'replacements' in bb[i][list(bb[i].keys())[0]]:
        replacements.append(bb[i][list(bb[i].keys())[0]]['replacements'])
    else:
        replacements.append(None)
    if 'wicket' in bb[i][list(bb[i].keys())[0]]:
        w.append(bb[i][list(bb[i].keys())[0]]['wicket'])
    else:
        w.append(0)
    if 'extras' in bb[i][list(bb[i].keys())[0]]:
        extras.append(bb[i][list(bb[i].keys())[0]]['extras'])
    else:
        extras.append(0)

over_batsman=[]
over_extras=[]
over_total=[]
for i in range(len(rs)):
    over_batsman.append(rs[i]['batsman'])
    over_extras.append(rs[i]['extras'])
    over_total.append(rs[i]['total'])
    
wides=[]
legbyes=[]
byes=[]
noballs=[]
penalty=[]
for i in range(len(extras)):
    if type(extras[i])==int:
        wides.append(0)
        legbyes.append(0)
        byes.append(0)
        noballs.append(0)
        penalty.append(0)
    else:
        if 'wides' in extras[i]:
            wides.append(extras[i]['wides'])
        else:
            wides.append(0)
        if 'legbyes' in extras[i]:
            legbyes.append(extras[i]['legbyes'])
        else:
            legbyes.append(0)
        if 'byes' in extras[i]:
            byes.append(extras[i]['byes'])
        else:
            byes.append(0)
        if 'noballs' in extras[i]:
            noballs.append(extras[i]['noballs'])
        else:
            noballs.append(0)
        if 'penalty' in extras[i]:
            penalty.append(extras[i]['penalty'])
        else:
            penalty.append(0)
            
fielder=[]
kind=[]
player_out=[]
for i in range(len(w)):
    if type(w[i])==int:
        fielder.append(None)
        kind.append(None)
        player_out.append(None)
    else:
        if 'fielders' in w[i]:
            fielder.append(w[i]['fielders'][0])
        else:
            fielder.append(None)
        if 'kind' in w[i]:
            kind.append(w[i]['kind'])
        else:
            kind.append(None)
        if 'player_out' in w[i]:
            player_out.append(w[i]['player_out'])
        else:
            player_out.append(None)
            
            


replace_in=[]
replace_out=[]
replace_reason=[]
replace_role=[]  
for i in range(len(replacements)):
    if replacements[i]==None:
            replace_in.append(None)
            replace_out.append(None)
            replace_reason.append(None)
            replace_role.append(None)
    else: 
        if 'in' in replacements[i]['role'][0]:
            replace_in.append(replacements[i]['role'][0]['in'])
        else:
            replace_in.append(None)
        if 'out' in replacements[i]['role'][0]:
            replace_out.append(replacements[i]['role'][0]['out'])
        else:
            replace_out.append(None)
        if 'reason' in replacements[i]['role'][0]:
            replace_reason.append(replacements[i]['role'][0]['reason'])
        else:
            replace_reason.append(None)
        if 'role' in replacements[i]['role'][0]:
            replace_role.append(replacements[i]['role'][0]['role'])
        else:
            replace_role.append(None)
over_no=[]
import math 
for i in range(len(ball_no)):
    over_no.append(int(str(ball_no[i]).split('.')[0]))
    ball_no[i]=int(str(ball_no[i]).split('.')[1])
day=[]
month=[]
year=[]
for i in range(len(dates)):
    year.append(str(dates[i]).split('-')[0])
    month.append(str(dates[i]).split('-')[1])
    day.append(str(dates[i]).split('-')[2])

d=dict()
d['match_no']=match
d['innings']=innings
d['day']=day
d['month']=month
d['year']=year
d['team1']=team1
d['team2']=team2
d['team_batting']=tp
d['over_no']=over_no
d['ball_no']=ball_no
d['batsman']=batsman
d['bowler']=bowler
d['non_striker']=non_striker
d['runs_scored_batsman']=over_batsman
d['extra_runs_ball']=over_extras
d['byes']=byes
d['legbyes']=legbyes
d['no_balls']=noballs
d['penalty']=penalty
d['wides']=wides
d['total_runs_in_ball']=over_total
d['kind']=kind
d['player_out']=player_out
d['fielder']=fielder
d['player_in_replacement']=replace_in
d['player_out_replacement']=replace_out
d['player_reason_replacement']=replace_reason
d['player_role_replacements']=replace_role

import pandas as pd
df=pd.DataFrame(d)
df.to_csv('/home/god/data/ipl/ipl.csv')

            
