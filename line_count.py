#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8
import re
import os
import csv

# Input the path you would like to get the list of files
path = "C:\\Users\\engdep\\Desktop\\pleiades\\workspace\\Jiryu_Kaiseki_pc1"
# datee = "161111_1718"
seiki_fold = re.compile("\d+_\d+")
seiki_csv = re.compile("TRJ.+csv")

# Get folders list under the path

rrr = []

def jud1(x,y,dirn):
    if x >= 37000 and x < 38000 and y >= 25000 and y < 35000 and dirn > -45 and dirn < 45:
        return True
    else:
        return False

def jud2(x,y,dirn):
    if x >= 58000 and x < 62000 and y >= 29000 and y < 30000 and dirn > 45 and dirn < 135:
        return True
    else:
        return False

def jud3(x,y,dirn):
    if x >= 70000 and x < 74000 and y >= 30000 and y < 31000 and dirn > 45 and dirn < 135:
        return True
    else:
        return False

def jud4(x,y,dirn):
    if x >= 100500 and x < 101500 and y >= 40000 and y < 50000 and ((dirn >= -180 and dirn < -135) or (dirn > 135 and dirn <= 180)):
        return True
    else:
        return False
def jud5(cat):
    if cat == "1" or cat == "2":
        return True
    else:
        return False

def extr_fld(roww):
    output = seiki_fold.search(roww)
    return output

def idcheck(id, list):
    for tip in list:
        if tip == id:
            return True
    return False

# A function that returns a regular expression match object to create a list of csv files
def extr_csv(row):
    output = seiki_csv.match(row)
    return output

list_dirr = os.listdir(path)
for row in list_dirr:
    if os.path.isdir(path + "\\" + row) == True and extr_fld(row) != None:
        rrr.append(extr_fld(row).group())

# Change here to select data folders set
print(rrr)
print(len(rrr))
# del rrr[12:40]

# del rrr[0:12]
# del rrr[16:40]

del rrr[0:28]
print(rrr)
print(len(rrr))


"""
f2 = open(path + "\\" + datee + "\\" + datee + '_integrated.csv', 'w+', newline="")
datawriter = csv.writer(f2)
datawriter.writerow(["unixtime","id","x","y","z","velocity","direction","acceleration","ang_velocity","category","grid_id","area_id","size"])
"""

# Process to append the matched csv file name path group to the arr1 list
arr1 = []
for x1 in rrr:
    list_dir = os.listdir(path + "\\" + x1)
    for row in list_dir:
        if extr_csv(row) != None:
            arr1.append(path + "\\" + x1 + "\\" + extr_csv(row).group())

# [MAIN]Process to sequentially read and integrate csv stored in arr1
i = 0
total = 0
totala = 0
totalb = 0
totalc = 0
totald = 0
rowa = []
rowb = []
rowc = []
rowd = []
id_list= []
check1_count = 0
check2_count = 0
check3_count = 0
firstflag = True
error_list = []

while i < len(arr1):
    if firstflag == True:
        firstflag = False
        checker = extr_fld(arr1[i]).group()
    print(i,"th loop.",arr1[i]," is starting")
    f1 = open(arr1[i],"r")
    datareader = csv.reader(f1)
    for line in datareader:
        # Need more strict condition
        # if len(line)==24 or len(line)==14:
        x = float(line[2])
        y = float(line[3])
        d = float(line[6])
        check1_count = check1_count + 1
        if jud1(x,y,d) == True or jud2(x,y,d) == True or jud3(x,y,d) == True or jud4(x,y,d) == True:
            # datawriter.writerow(line)
            # print("CHECK2 OK!")
            check2_count = check2_count + 1
            if idcheck(float(line[1]),id_list) == False:
                # print("CHECK3 OK!")
                check3_count = check3_count + 1
                id_list.append(float(line[1]))
                total = total + 1
                if extr_fld(arr1[i]).group() == checker:
                    if jud1(x,y,d) == True:
                        totala = totala + 1
                    elif jud2(x,y,d) == True:
                        totalb = totalb + 1
                    elif jud3(x,y,d) == True:
                        totalc = totalc + 1
                    elif jud4(x,y,d) == True:
                        totald = totald + 1
                else:
                    checker = extr_fld(arr1[i]).group()
                    rowa.append(totala)
                    rowb.append(totalb)
                    rowc.append(totalc)
                    rowd.append(totald)
                    totala = 0
                    totalb = 0
                    totalc = 0
                    totald = 0
                    if jud1(x,y,d) == True:
                        totala = totala + 1
                    elif jud2(x,y,d) == True:
                        totalb = totalb + 1
                    elif jud3(x,y,d) == True:
                        totalc = totalc + 1
                    elif jud4(x,y,d) == True:
                        totald = totald + 1
            #else:
                #print(float(line[1]))
        #else:
            #print(x,y,d)
    print("checked file:",arr1[i])
    print(rowa)
    print(rowb)
    print(rowc)
    print(rowd)
    f1.close()
    i = i + 1

rowa.append(totala)
rowb.append(totalb)
rowc.append(totalc)
rowd.append(totald)
print("The total is " + str(total))
print(rowa)
print(rowb)
print(rowc)
print(rowd)
print("Error list;",error_list)
print("ProgramEND")
