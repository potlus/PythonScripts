# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:31:39 2019

@author: potlus
"""

import pandas as pd
from pandas import DataFrame

#Read File Path
path = 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv'
cmdb = pd.read_csv(path, header=0,encoding = 'unicode_escape')
cmdb.shape
df = DataFrame(cmdb, columns= ['Sys_Id', 'SW_Name', 'Technical_Lead', 'Support_Group', 'Operational_Status'])

Export = df.to_json (r'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/sampleCMDB.json', orient='records', lines=True)