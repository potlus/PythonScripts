# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:41:38 2019

@author: potlus
"""

import csv, json

csvfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'rU')
jsonfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.json', 'w')

reader = csv.DictReader(csvfile)

for row in reader:
    json.dump({ row['Sys_Id'] : (row['SW_Name'], row['Technical_Lead'], row['Support_Group'], row['Operational_Status']) }, jsonfile)
    jsonfile.write('\n')