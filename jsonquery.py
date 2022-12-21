import json
file = open("database.json",'r')
f = json.load(file)
for i in f['emp_details']:
    print(i)