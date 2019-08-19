# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 07:52:24 2019

@author: Sreenivas

#Python Script or converting CSV to JSON
"""

import csv
import json

csvfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'r')
jsonfile = 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/testdata.json'

reader = csv.DictReader(csvfile)

with open(jsonfile, 'a') as csvfile:
	for x in reader:
		json.dump (x, csvfile)
		csvfile.write('\n')