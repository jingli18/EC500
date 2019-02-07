#!/usr/bin/python
import json
import os

# patient_dic = {'blood_pressure':120, 'blood_oxgen':12, 'heart_rate':80}

json_dir = os.getcwd()
# with open(json_dir + "\\patient.json","w") as write:
#     json.dump(patient_dic, write)
#     print("Json Loaded!")

with open(json_dir + "\\patient.json","r") as read:
    new_patient_dic = json.load(read)
    print(new_patient_dic)
    print("Json Read!")
def control():
    key = input("Enter the date you want to check: ")
    if key != 'c' :
        print(new_patient_dic[key])
        control()
    return 0

control()