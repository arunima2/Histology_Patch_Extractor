import json
import sys
import os
import subprocess

input_file = sys.argv[1]
output_folder = sys.argv[2]
patch_sq_size = sys.argv[3]
f1 = os.path.basename(input_file)
f2,f3 = os.path.splitext(f1)

with open(os.path.dirname(input_file)+"/"+f2+".json") as json_file:
    data = json.load(json_file)
    cohorts = data.keys()
    num_cohorts = len(cohorts)
    for ch in cohorts:
        if not os.path.exists(output_folder+"/"+ch):
            os.makedirs(output_folder+"/"+ch)
        counter = 1
        for p in data[ch]:
            subprocess.call(["python" ,"patch_extraction.py",input_file,patch_sq_size,str(p['x']),str(p['y']),output_folder+"/"+ch,str(counter)])
            print('x: ' + str(p['x']))
            print('y: ' + str(p['y']))
            counter+=1
