#coding:utf-8

import csv
import matplotlib.pyplot as plt
import os
import datetime

pathin = "C:\\Users\\1500570\\Documents\\R\\WS\\dataset_akihabara"
lister = os.listdir(pathin)
os.mkdir(pathin+"\\fig")
i= 0
datafx = []
datafy = []
tempx = []
tempy = []
tempv = []
span = 1800
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
            plt.xlim([0,20000])
            plt.ylim([0,20000])
            plt.scatter(tempx,tempy,alpha=0.01,s=0.5,c=tempv,cmap="plasma")
            plt.colorbar()
            plt.savefig(pathin+"\\fig\\test"+str(counter)+".png")
            plt.close()
            first = first + span
            tempx = []
            tempy = []
            tempv = []
            tempx.append(int(line[2]))
            tempy.append(int(line[3]))
            tempv.append(float(line[5]))
            counter += 1
        else:
            tempx.append(int(line[2]))
            tempy.append(int(line[3]))
            tempv.append(float(line[5]))
    i += 1

plt.title(str(datetime.datetime.fromtimestamp(first)))
plt.xlim([0,20000])
plt.ylim([0,20000])
plt.scatter(tempx,tempy,alpha=0.1,s=0.5,c=tempv,cmap="plasma")
plt.colorbar()
plt.savefig(pathin+"\\fig\\test"+str(counter)+".png")
plt.close()
tempx = []
tempy = []
tempv = []
tempx.append(int(line[2]))
tempy.append(int(line[3]))
tempv.append(float(line[5]))

print(datafx)
