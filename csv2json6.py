## -*- coding: utf-8 -*-
#"""
#Created on Thu Jul  4 09:41:03 2019
#
#@author: potlus
#"""
#
#import csv
#import pandas as pd
#path = 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/'
#file = 'SN_CMDB_Apps.csv'
#f = open(path+file,'rt')
#columns = ("Sys_Id", "SW_Name", "Technical_Lead", "Support_Group", "Operational_Status")
#reader = csv.reader(f)
#
##once contents are available, I then put them in a list
#csv_list = []
#for l in reader:
#    csv_list.append(l)
#f.close()
##now pandas has no problem getting into a df
#df = pd.DataFrame(csv_list, columns= ['Sys_Id', 'SW_Name', 'Technical_Lead', 'Support_Group', 'Operational_Status'])
#Export = df.to_json (r'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/sampleCMDB.json', orient='records', lines=True)


import csv
import json
csvfile = csv.DictReader('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'r')
output =[]
for each in csvfile:
    row ={}
    row['Sys_Id'] = each['Sys_Id']
    row['SW_Name']  = each['SW_Name']
    row['Support_Group']  = each ['Support_Group']
    row['Operational_Status']   = each['Operational_Status']
    output.append(row)
json.dump(output,open('filename.json','w'),indent=4,sort_keys=False)