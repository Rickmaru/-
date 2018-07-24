#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

#path下に複数のcsvを入れると一括で計算します

import numpy as np
import csv
import os

path = "C:\\Users\\1500570\\Documents\\R\\WS\\dataset_a4\\testdir"

lister = os.listdir(path)
ff = True
mat = []
for list in lister:
    ren = csv.reader(open(path+"\\"+str(list),"r+"))
    for line in ren:
        if ff == True:
            ff = False
            mat.append(line)
        else:
            mat.append(line)
        # if len(mat) % 1000 == 0: print(len(mat))

mat = np.array(mat)
print(len(mat))
print(mat[0])
np.delete(mat, 12, axis=1)
print(mat[0])
print(mat[:,1:2])
id_arr = len(list(set(mat[:,0:1])))
print(len(id_arr))

