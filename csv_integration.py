#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8
import re
import os
import csv

# Input the path you would like to get the list of files
path = "C:\\Users\\1500570\\Desktop\\pleiades\\workspace\\Jinryu_Kaiseki"
# datee = "161111_1718"
seiki_fold = re.compile("\d+_\d+")
seiki_csv = re.compile("TRJ.+csv")

# Get folders list under the path

rrr = []

def extr_fld(roww):
    output = seiki_fold.match(roww)
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
# del rrr[8:36]
del rrr[0:8]
del rrr[15:28]
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
totala= 0
totalb = 0
totalc = 0
totald = 0
id_list= []
check1_count = 0
check2_count = 0
check3_count = 0
firstflag = False
error_list = []

while i < len(arr1):
    if firstflag == True:
        firstflag = False
        i = i + 1
        continue
    print(i,"th loop.",arr1[i]," is starting")
    f1 = open(arr1[i],"r")
    datareader = csv.reader(f1)
    for line in datareader:
        # Need more strict condition
        if len(line)==24 or len(line)==14:
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
    ttotal = totala + totalb + totalc + totald
    print("[result]total = ",total,totala,totalb,totalc,totald,ttotal)
    f1.close()
    i = i + 1

print("The total is " + str(total))
print("Partly totals are ",totala,totalb,totalc,totald,"checksum:",totala+totalb+totalc+totald)
print("Error list;",error_list)
print("finished")
