import json
import csv

# with open("json_file.json","r") as file:
#     data=json.load(file)
#
# with open("json_to_csv.csv","w") as file:
#     csv_file=csv.writer(file)
#     csv_file.writerow(["name","Lastname"])
#     for item in data["students"]:
#         csv_file.writerow([item['name'],item['lastname']])

def Convert_json_to_csv(json_file,csv_file):
    with open(json_file,'r') as file:
        data=json.load(file)

    with open(csv_file,'w') as file:
        csv_write=csv.writer(file)
        csv_write.writerow(['name','Lastname'])
        for item in data["students"]:
            csv_write.writerow([item['name'],item['lastname']])

Convert_json_to_csv('json_file.json','json_csv.csv')

















