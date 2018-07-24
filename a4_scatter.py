#coding:utf-8

import csv
import matplotlib.pyplot as plt
import os
import datetime

pathin = "C:\\Users\\1500570\\Documents\\R\\WS\\dataset_a4"
lister = os.listdir(pathin)
os.mkdir(pathin+"\\fig")
i= 0
datafx = []
datafy = []
tempx = []
tempy = []
tempv = []

# test
tempx2 = []
tempy2 = []
tempv2 = []

def area_jud(l1,l2,x_min,x_max,y_min,y_max):
    if int(l1) > x_min and int(l1) < x_max and int(l2) > y_min and int(l2) < y_max:
        return True
    else:
        return False

def v_jud(vel,v_min,v_max):
    if float(vel) > v_min and float(vel) < v_max:
        return True
    else:
        return False

span = 3600*24
ff = True
counter = 0
while i < len(lister):
    data = csv.reader(open(pathin+"\\"+lister[i],"r"))
    for line in data:
        if ff == True:
            print(line[0])
            first = int(float(line[0]))-int(float(line[0]))%span
            print("first",datetime.datetime.fromtimestamp(first))
            ff = False
        if float(line[0]) >= first+span:
            plt.title(str(datetime.datetime.fromtimestamp(first)))
            plt.xlim([0,25000])
            plt.ylim([0,25000])
            plt.scatter(tempx2,tempy2,alpha=0.01,s=1,c="red")
            plt.scatter(tempx,tempy,alpha=0.005,s=1,c=tempv,cmap="plasma")
            plt.colorbar()
            plt.savefig(pathin+"\\fig\\"+str(datetime.datetime.fromtimestamp(first)).replace(":","..")+".png", format='png', dpi=300)
            plt.close()
            first = first + span
            tempx = []
            tempy = []
            tempv = []
            # test
            tempx2 = []
            tempy2 = []
            tempv2 = []
            # if area_jud(line[2], line[3], 25000, 30000, 30000, 35000)==True:
            # if v_jud(line[5], 0.1, 2.0) == True:
            if int(line[9]) == 2:
                tempx2.append(int(line[2]))
                tempy2.append(int(line[3]))
                tempv2.append(float(line[5]))
            else:
                tempx.append(int(line[2]))
                tempy.append(int(line[3]))
                tempv.append(float(line[5]))
            counter += 1
        else:
            # if area_jud(line[2], line[3], 25000, 30000, 30000, 35000)==True:
            # if v_jud(line[5], 0.1, 2.0) == True:
            if int(line[9]) == 2:
                tempx2.append(int(line[2]))
                tempy2.append(int(line[3]))
                tempv2.append(float(line[5]))
            else:
                tempx.append(int(line[2]))
                tempy.append(int(line[3]))
                tempv.append(float(line[5]))
    i += 1

plt.title(str(datetime.datetime.fromtimestamp(first)))
plt.xlim([0,25000])
plt.ylim([0,25000])
plt.scatter(tempx,tempy,alpha=0.1,s=1,c=tempv,cmap="plasma")
plt.colorbar()
plt.savefig(pathin+"\\fig\\"+str(datetime.datetime.fromtimestamp(first)).replace(":","..")+".png", format='png', dpi=300)
plt.close()
tempx = []
tempy = []
tempv = []
# test
tempx2 = []
tempy2 = []
tempv2 = []
# if v_jud(line[5], 0.1, 2.0) == True:
# if area_jud(line[2], line[3], 25000, 30000, 30000, 35000)==True:
if int(line[9]) == 2:
    tempx2.append(int(line[2]))
    tempy2.append(int(line[3]))
    tempv2.append(float(line[5]))
else:
    tempx.append(int(line[2]))
    tempy.append(int(line[3]))
    tempv.append(float(line[5]))

print(datafx)
