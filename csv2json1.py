# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:12:41 2019

@author: potlus
"""

import csv
import json

csvfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'rU')
jsonfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/testdata.json', 'w')

reader = csv.DictReader(csvfile)

for row in reader:
    json.dump({ row['Sys_Id'] : (row['SW_Name'], row['Technical_Lead'], row['IT_Owner'], row['Operational_Status']) }, jsonfile)
    jsonfile.write('\n')