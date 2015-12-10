
# coding: utf-8

# In[1]:

import csv
import pandas as pd
import numpy as np
data=pd.read_csv('epl\epldata11.csv', header=0)
originaldata=data=pd.read_csv('epl\epldata11.csv', header=0)
KP=5

k=[0]*len(data)

data['HomePastGoals']=np.asarray(k)
data['AwayPastGoals']=np.asarray(k)
data['HomePastShots']=np.asarray(k)
data['AwayPastShots']=np.asarray(k)
data['HomePastTarget']=np.asarray(k)
data['AwayPastTarget']=np.asarray(k)
data['HomePastCorners']=np.asarray(k)
data['AwayPastCorners']=np.asarray(k)

def pastgoals(myTeam):
    dataSub = data[(data['HomeTeam'] == myTeam) | (data['AwayTeam'] == myTeam)]
    myList = []
    
    for i in range(0,len(dataSub)):
        if dataSub.HomeTeam.iloc[i] == myTeam:
            myList.append(dataSub.HG.iloc[i])
        else:
            myList.append(dataSub.AG.iloc[i])
            
    dataSub['MyTeamGoals'] = np.asarray(myList)
    
    dataSub['kPgoal'] = (np.cumsum(dataSub['MyTeamGoals']) - np.cumsum(dataSub['MyTeamGoals']).shift(KP))/KP

    
 


    for i in dataSub.index:
        if data.iloc[i].HomeTeam==myTeam:
            data['HomePastGoals'][i]= dataSub.loc[i].kPgoal
        if data.iloc[i].AwayTeam==myTeam:
            data['AwayPastGoals'][i]= dataSub.loc[i].kPgoal
            
    return (data)

def pastshots(myTeam):
    dataSub = data[(data['HomeTeam'] == myTeam) | (data['AwayTeam'] == myTeam)]
    myList = []
    
    for i in range(0,len(dataSub)):
        if dataSub.HomeTeam.iloc[i] == myTeam:
            myList.append(dataSub.HS.iloc[i])
        else:
            myList.append(dataSub.AS.iloc[i])
            
    dataSub['MyTeamShots'] = np.asarray(myList)
    
    dataSub['kPshot'] =( np.cumsum(dataSub['MyTeamShots']) - np.cumsum(dataSub['MyTeamShots']).shift(KP))/KP

    
 


    for i in dataSub.index:
        if data.iloc[i].HomeTeam==myTeam:
            data['HomePastShots'][i]= dataSub.loc[i].kPshot
        if data.iloc[i].AwayTeam==myTeam:
            data['AwayPastShots'][i]= dataSub.loc[i].kPshot
            
    return (data)

def pasttarget(myTeam):
    dataSub = data[(data['HomeTeam'] == myTeam) | (data['AwayTeam'] == myTeam)]
    myList = []
    
    for i in range(0,len(dataSub)):
        if dataSub.HomeTeam.iloc[i] == myTeam:
            myList.append(dataSub.HST.iloc[i])
        else:
            myList.append(dataSub.AST.iloc[i])
            
    dataSub['MyTeamShotsonTarget'] = np.asarray(myList)
    
    dataSub['kPtarget'] = (np.cumsum(dataSub['MyTeamShotsonTarget']) - np.cumsum(dataSub['MyTeamShotsonTarget']).shift(KP))/KP
    for i in dataSub.index:
        if data.iloc[i].HomeTeam==myTeam:
            data['HomePastTarget'][i]= dataSub.loc[i].kPtarget
        if data.iloc[i].AwayTeam==myTeam:
            data['AwayPastTarget'][i]= dataSub.loc[i].kPtarget
            
    return (data)

def pastcorner(myTeam):
    dataSub = data[(data['HomeTeam'] == myTeam) | (data['AwayTeam'] == myTeam)]
    myList = []
    
    for i in range(0,len(dataSub)):
        if dataSub.HomeTeam.iloc[i] == myTeam:
            myList.append(dataSub.HC.iloc[i])
        else:
            myList.append(dataSub.AC.iloc[i])
            
    dataSub['MyCorner'] = np.asarray(myList)
    
    dataSub['kPCorner'] = (np.cumsum(dataSub['MyCorner']) - np.cumsum(dataSub['MyCorner']).shift(KP))/KP

    
 


    for i in dataSub.index:
        if data.iloc[i].HomeTeam==myTeam:
            data['HomePastCorners'][i]= dataSub.loc[i].kPCorner
        if data.iloc[i].AwayTeam==myTeam:
            data['AwayPastCorners'][i]= dataSub.loc[i].kPCorner
            
    return (data)

k=[0]*len(data)

data['HomeRecentRecord']=np.asarray(k)
data['AwayRecentRecord']=np.asarray(k)

def recentrecord(myTeam):
    dataSub = data[(data['HomeTeam'] == myTeam) | (data['AwayTeam'] == myTeam)]
    myList = []
    
    for i in range(0,len(dataSub)):
        if dataSub.HomeTeam.iloc[i] == myTeam:
            if dataSub.HR.iloc[i]=="H":
                myList.append(3)
            if dataSub.HR.iloc[i]=="D":
                myList.append(1)
            if dataSub.HR.iloc[i]=="A":
                myList.append(0)
        else:
            if dataSub.HR.iloc[i]=="H":
                myList.append(0)
            if dataSub.HR.iloc[i]=="D":
                myList.append(1)
            if dataSub.HR.iloc[i]=="A":
                myList.append(3)
            
    dataSub['Record'] = np.asarray(myList)
    dataSub['RecentRecord'] = np.cumsum(dataSub['Record']) - np.cumsum(dataSub['Record']).shift(5)
    
    for i in dataSub.index:
        if data.iloc[i].HomeTeam==myTeam:
            data['HomeRecentRecord'][i]= dataSub.loc[i].RecentRecord
        if data.iloc[i].AwayTeam==myTeam:
            data['AwayRecentRecord'][i]= dataSub.loc[i].RecentRecord
            
    return (data)


# In[2]:

teamlist=[]
for i in np.unique(originaldata['HomeTeam']):
   teamlist.append(i)

teamlist


# In[3]:

for i in range(0,len(teamlist)):
    pastgoals(teamlist[i])
    pastshots(teamlist[i])
    pasttarget(teamlist[i])
    pastcorner(teamlist[i])
    recentrecord(teamlist[i])

    
data
    


# In[4]:




# In[ ]:




# In[ ]:



