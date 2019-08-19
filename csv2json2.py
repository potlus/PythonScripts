# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:15:52 2019

@author: potlus
"""

# importing pandas package 
#import pandas as pd 

  
# making data frame from csv file  
#data = pd.read_csv("S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps1.csv",header=0,encoding = 'unicode_escape') 
  
# replacing blank spaces with '_'  
#data.columns =[column.replace(" ", "_") for column in data.columns] 
  
# filtering with query method 
#data.query('Operational_Status == "%s"' % Active) 
#data[data['Operational_Status'].str.contains(r'Active')]
#data.query('Operational_Status.str.contains("Active", na=False)', engine='python')  
#data = open( 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/parsed.json', 'w')  
#data.write(data)  
#print ("JSON saved!")
# display 
#data


#import csv
#import json
#import os
import pandas as pd
#os.chdir('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python')
#filename = 'SN_CMDB_Apps.csv'

cmdb = pd.read_csv('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv',header=0,encoding = 'unicode_escape', engine='python')
iFlowStatus = cmdb[cmdb['Operational_Status'].str.contains('iFlow', na=False)]['Active']
print(iFlowStatus)