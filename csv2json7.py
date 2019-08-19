import csv
import json
with open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    data_list = list()
    for row in reader:
        data_list.append(row)
data = [dict(zip(data_list[0],row)) for row in data_list]
data.pop(0)
s = json.dumps(data)
print (s)