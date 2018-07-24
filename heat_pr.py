#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8
import csv
import re

# Input the path you would like to get the list of files
fname = "161111_1718"
path = "C:\\Users\\1500570\\Desktop\\pleiades\\workspace\\Jinryu_Kaiseki\\" + fname

# These are constants for this program and should not be changed
arrx = []
arry = []
f1 = open(path + "\\" + fname + "_integrated.csv","r")
f2 = open(path + "\\" + fname + '_formap.csv', 'w+', newline="")
datareader = csv.reader(f1)
datawriter = csv.writer(f2)
dvde_grid = re.compile("\d+")
first = True

# Process to append x and y values to arrx and arry
for i in datareader:
    if first == True:
        first = False
        datawriter.writerow([i[2],i[3],i[6],"grid_x","grid_y"])
        continue
    tmp = dvde_grid.findall(i[10])
    if len(tmp) > 1:
        datawriter.writerow([i[2],i[3],i[6],int(i[2])//7000,int(i[3])//7000])

print("finished")