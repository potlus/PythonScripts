#import csv
#import json
#
#file = 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv'
#json_file = 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/sampleCMDB.json'
#
##Read CSV File
#def read_CSV(file, json_file):
#    csv_rows = []
#    with open(file) as csvfile:
#        reader = csv.DictReader(csvfile)
#        field = reader.fieldnames[1,2,4,11,12]
#        for row in reader:
#            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
#        convert_write_json(csv_rows, json_file)
#
##Convert csv data into json
#def convert_write_json(data, json_file):
#    with open(json_file, "w") as f:
#        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty
#        f.write(json.dumps(data))
#
#
#read_CSV(file,json_file)

#
#import csv
#import json
#
#csvfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'r')
#jsonfile = open('S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/sampleCMDB.json', 'w')
#
#fieldnames = ("Sys_Id","SW_Name","Technical_Lead","Support_Group","Operational_Status")
#reader = csv.DictReader(csvfile , fieldnames)
#
#code = ''
#for row in reader:
#        print('+' + row['Code'])
#        for key in row:
#            row[key] = row[key].decode('utf-8', 'ignore').encode('utf-8')      
#        json.dump(row, jsonfile)
#        jsonfile.write('\n')
##    except:
# #       print('-' + row['Code'])
#  #      raise


import csv
import json

csvfilename = 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv'
jsonfilename = csvfilename.split('.')[0] + '.json'
csvfile = open(csvfilename, 'r')
jsonfile = open(jsonfilename, 'w')
reader = csv.DictReader(csvfile)

fieldnames = ('Sys_Id', 'SW_Name', 'Technical_Lead', 'Support_Group', 'Operational_Status')

output = []

for each in reader:
  row = {}
  for field in fieldnames:
    row[field] = each[field]
output.append(row)

json.dump(output, jsonfile, indent=2, sort_keys=True)