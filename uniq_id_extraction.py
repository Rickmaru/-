#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import numpy as np
import csv
import os
import pandas as pd
from collections import Counter

path = "C:\\Users\\1500570\\Documents\\R\\WS\\dataset_a4"

ff = True
mat = []
i = 0

for onj in [ren for ren in [csv.reader(open(path+"\\"+str(list),"r+")) for list in os.listdir(path)]]:
    i += 1
    print(i)
    for line in onj:
        mat.append(line)

"""
for list in lister:
    i += 1
    ren = csv.reader(open(path+"\\"+str(list),"r+"))
    print(str(i)+" / "+str(len(lister)))
    for line in ren:
        mat.append(line)
"""
field = ["unixtime","id","x","y","z","velocity","direction","acceleration","ang_velocity","category","grid_id","area_id","size","un"]

idlist = [line[1] for line in mat]
c1= Counter(idlist)

# mat = np.array(mat)

def jud_human(matl):
    matmmx = [int(x[2]) for x in matl]
    matmmy = [int(y[3]) for y in matl]
    if max(matmmx) - min(matmmx) > 3000 or max(matmmy) - min(matmmy) > 3000:
        return True
    else:
        return False

rrei = csv.writer(open(path+"\\"+"iduniq2.csv", "w+", newline=""),delimiter=",")
for line in c1.most_common():
    mattemp = list(filter((lambda x:x[1]==line[0]), mat))
    if jud_human(mattemp) == True:
        rrei.writerow(line)
