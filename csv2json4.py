import csv  
import json  
  
#Declaration
csvFile = open( 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'r' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
fieldnames = ("Sys_Id", "SW_Name", "Technical_Lead", "Support_Group", "Operational_Status")
reader = csv.DictReader(csvFile, fieldnames)  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
#print "JSON parsed!" 
# Save the JSON  
jsonFile = open( 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/parsed.json', 'w')  
jsonFile.write(out)  
#print "JSON saved!"