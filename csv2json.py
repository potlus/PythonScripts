import csv  
import json  
  
# Open the CSV  
f = open( 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/SN_CMDB_Apps.csv', 'rU' )  
# Change each fieldname to the appropriate field name. I know, so difficult.  
reader = csv.DictReader( f, fieldnames = ( "fieldname0","fieldname1","fieldname2","fieldname3" ))  
# Parse the CSV into JSON  
out = json.dumps( [ row for row in reader ] )  
print ("JSON parsed!")
# Save the JSON  
f = open( 'S:/DATA CENTER/Autosys/Working On/Sreenivas/SCRIPTS/Python/parsed.json', 'w')  
f.write(out)  
print ("JSON saved!")