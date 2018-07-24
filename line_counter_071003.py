#author:R.Kunimoto, TAKENAKA co.
#coding:utf-8
import re
import os
import csv
import datetime
import math


# Input the path you would like to get the list of files
path = "C:\\Users\\1500570\\Documents\\R\\WS\\dataset_a4"

seiki_fold = re.compile("\d+_\d+")
seiki_csv = re.compile("TRJ.+csv")

rrr = []
i = 0

total_ell_s = 0
total_ell_1d = []

firstflag = True

arg_move = 40
"""
# 0712_aoyama_in
mat_judge_2d = [
    [5000,10000,-7500,1000,45,arg_move],
    [20000,70000,2000,4000,90,arg_move],
    [68000,70000,0,18000,180,arg_move],
    [65000,70000,40000,48000,-135,arg_move],
    [57500,62000,38000,44000,-90,arg_move],
    [22000,30000,33000,36000,-50,arg_move],
    [8000,18000,33000,36000,-90,arg_move],
    [8000,10000,20000,30000,0,arg_move],
    [4000,8000,4000,10000,0,arg_move]
    ]
"""
# 0712_aoyama_in
mat_judge_2d = [
    [3500,5700,3500,3600,-90,arg_move,False],
    [5400,5500,-1,3500,5000,45,arg_move,True],
    [6400,6500,4000,6000,25,arg_move,False],
    [10500,10600,-1,6750,7500,-135,arg_move,True],
    [7300,7400,500,2500,180,arg_move,False],
    [-1100,-1000,0.5,7500,8600,120,arg_move,True],
    [9000,9100,6000,7000,180,arg_move,False],
    [9000,9100,3750,4750,180,arg_move,False],
    [9400,9500,1000,2750,0,arg_move,False],
    [9500,11000,3500,3600,-90,arg_move,False],
    [12000,12100,4500,6500,0,arg_move,False],
    [12400,12500,2250,3250,-160,arg_move,False],
    [13000,15000,6500,6600,-90,arg_move,False],
    [13500,15500,4400,4500,90,arg_move,False],
    [-4550,-4450,0.5,13950,14950,-60,arg_move,True],
    [13900,14000,1000,2000,0,arg_move,False],
    [16750,16850,5000,6500,180,arg_move,False],
    [11500,11600,-0.5,17250,18500,60,arg_move,True],
    [20500,20600,4000,6000,0,arg_move,False],

    [3500,5700,3500,3600,90,arg_move,False],
    [5400,5500,-1,3500,5000,-135,arg_move,True],
    [6400,6500,4000,6000,-155,arg_move,False],
    [10500,10600,-1,6750,7500,45,arg_move,True],
    [7300,7400,500,2500,0,arg_move,False],
    [-1100,-1000,0.5,7500,8600,-60,arg_move,True],
    [9000,9100,6000,7000,0,arg_move,False],
    [9000,9100,3750,4750,0,arg_move,False],
    [9400,9500,1000,2750,180,arg_move,False],
    [9500,11000,3500,3600,90,arg_move,False],
    [12000,12100,4500,6500,180,arg_move,False],
    [12400,12500,2250,3250,20,arg_move,False],
    [13000,15000,6500,6600,90,arg_move,False],
    [13500,15500,4400,4500,-90,arg_move,False],
    [-4550,-4450,0.5,13950,14950,120,arg_move,True],
    [13900,14000,1000,2000,180,arg_move,False],
    [16750,16850,5000,6500,0,arg_move,False],
    [11500,11600,-0.5,17250,18500,-120,arg_move,True],
    [20500,20600,4000,6000,180,arg_move,False]
    ]

# 0728_aoyama
"""
mat_judge_2d = [
    [5000,10000,-7500,1000,45,arg_move],
    [20000,70000,2000,4000,90,arg_move],
    [68000,70000,0,18000,180,arg_move],
    [61000,70000,42000,48000,-135,arg_move],
    [54000,60000,40000,44000,-90,arg_move],
    [20000,30000,33500,35500,-50,arg_move],
    [7000,14000,30000,36000,-90,arg_move],
    [6500,8500,20000,30000,0,arg_move],
    [4000,8000,4000,10000,0,arg_move]
    ]
"""
# Para
mins = 1800
num_id = 100
wid = 100
vel = 0.1
num_gl = len(mat_judge_2d)
total_mat_1d = [0 for i in range(num_gl)]
row_mat_2d = [[] for i in range(num_gl)]

def judgement(x,y,dir,cndt):
    global wid
    wid2 = wid/2
    if cndt[-1] == False:
        if cndt[4] < 180-cndt[5]/2 and cndt[4] > -180+cndt[5]/2:
            if (x > cndt[0]-wid2 and x < cndt[1]+wid2) and (y > cndt[2]-wid2 and y < cndt[3]+wid2) and ((dir > cndt[4]-cndt[5]/2) and (dir < cndt[4]+cndt[5]/2)):
                return True
            else:
                return False
        elif cndt[4] > 0:
            if (x > cndt[0]-wid2 and x < cndt[1]+wid2) and (y > cndt[2]-wid2 and y < cndt[3]+wid2) and ((dir > cndt[4]-cndt[5]/2) or (dir < -180+(cndt[4]+cndt[5]/2-180))):
                return True
            else:
                return False
        elif cndt[4] < 0:
            if (x > cndt[0]-wid2 and x < cndt[1]+wid2) and (y > cndt[2]-wid2 and y < cndt[3]+wid2) and ((dir < cndt[4]+cndt[5]/2) or (dir > 180-(cndt[5]/2-(180+cndt[4])))):
                return True
            else:
                return False
    elif cndt[-1] == True:
        if cndt[5] < 180-cndt[6]/2 and cndt[5] > -180+cndt[6]/2:
            if (x > cndt[3] and x < cndt[4]) and (cndt[0] -wid2 +cndt[2]*x -y < 0) and (cndt[1] +wid2 +cndt[2]*x -y > 0) and ((dir > cndt[5]-cndt[6]/2) and (dir < cndt[5]+cndt[6]/2)):
                return True
            else:
                return False
        elif cndt[5] > 0:
            if (x > cndt[3] and x < cndt[4]) and (cndt[0] -wid2 +cndt[2]*x -y < 0) and (cndt[1] +wid2 +cndt[2]*x -y > 0) and ((dir > cndt[5]-cndt[6]/2) or (dir < -180+(cndt[5]+cndt[6]/2-180))):
                return True
            else:
                return False
        elif cndt[5] < 0:
            if (x > cndt[3] and x < cndt[4]) and (cndt[0] -wid2 +cndt[2]*x -y < 0) and (cndt[1] +wid2 +cndt[2]*x -y > 0) and ((dir < cndt[5]+cndt[6]/2) or (dir > 180-(cndt[6]/2-(180+cndt[5])))):
                return True
            else:
                return False

def judge_ellipse(cx,cy,dx,dy,x,y,IN):
    if IN == True:
        if ((x-cx)**2/dx**2) + ((y-cy)**2/dy**2) <= 1:
            return True
        else:
            return False
    elif IN == False:
        if ((x-cx)**2/dx**2) + ((y-cy)**2/dy**2) < 1:
            return True
        else:
            return False

def judge_dir(cx,cy,x,y,dir,IN):
    global arg_move
    if IN == True:
        corr = math.degrees(math.atan2(-(cy-y),-(cx-x)))
    elif IN == False:
        corr = math.degrees(math.atan2((cy-y),(cx-x)))
    if corr < 180-arg_move/2 and corr > -180+arg_move/2:
        if (dir > corr-arg_move/2) and (dir < corr+arg_move/2):
            return True
        else:
            return False
    elif corr >= 0:
        if (dir > corr-arg_move/2) or (dir < -180+(corr+arg_move/2-180)):
            return True
        else:
            return False
    elif corr < 0:
        if (dir < corr+arg_move/2) or (dir > 180-(-corr+arg_move/2-180)):
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

def extr_csv(row):
    output = seiki_csv.match(row)
    return output

# Create folders list;rrr

list_dirr = os.listdir(path)
for row in list_dirr:
    if os.path.isdir(path + "\\" + row) == True and extr_fld(row) != None:
        rrr.append(extr_fld(row).group())

# Change here to select data folders set
print("folders list[rrr]:",rrr)
print("length of rrr:",len(rrr))


# del rrr[12:40]
# del rrr[0:12]
# del rrr[16:40]
# del rrr[0:28]

# print(rrr)
# print(len(rrr))

"""
f2 = open(path + "\\" + datee + "\\" + datee + '_integrated.csv', 'w+', newline="")
datawriter = csv.writer(f2)
datawriter.writerow(["unixtime","id","x","y","z","velocity","direction","acceleration","ang_velocity","category","grid_id","area_id","size"])
"""

# Process to append the matched csv file name path group to the arr1 list
arr1 = []
"""
for x1 in rrr:
    list_dir = os.listdir(path + "\\" + x1)
    for row in list_dir:
        if extr_csv(row) != None:
            arr1.append(path + "\\" + x1 + "\\" + extr_csv(row).group())
"""
arr1 = os.listdir(path)
print("Length of files list:",len(arr1))

id_list = [[] for i in range(num_gl)]
id_list_ell = []

# main():
while i < len(arr1):
    with open(path+"\\"+arr1[i],"r") as f1:
        datareader = csv.reader(f1)
        print (i+1,"/",len(arr1),"th file is starting")
        # print ("The length of each row is,", len(rowa),"rowa is",rowa)
        # Subscript partial counted
        for line in datareader:
            # Need more strict condition?
            # if len(line)==24 or len(line)==14:
            t = float(line[0])
            x = float(line[2])
            y = float(line[3])
            d = float(line[6])
            c = int(line[9])
            v = float(line[5])
            id = float(line[1])
            if firstflag == True:
                firstflag = False
                comtime = t - t%mins
                firsttime = comtime
            while comtime + mins <= t:
                print(datetime.datetime.fromtimestamp(comtime))
                print(total_mat_1d)
                print(total_ell_1d)
                comtime += mins
                tcm = 0
                while tcm < num_gl:
                    row_mat_2d[tcm].append(total_mat_1d[tcm])
                    tcm += 1
                total_ell_1d.append(total_ell_s)
                total_mat_1d = [0 for i in range(num_gl)]
                total_ell_s = 0
            # check1_count = check1_count + 1
            jn = 0
            while jn < num_gl:
                if (v > vel) and (c == 2) and (idcheck(id, id_list[jn])==False) and (judgement(x, y, d, mat_judge_2d[jn]) == True):
                    id_list[jn].append(id)
                    if len(id_list[jn]) > num_id:
                        id_list[jn].pop()
                    total_mat_1d[jn] += 1
                jn += 1
            """
            if (
                idcheck(id, id_list_ell)==False
                #12_in
                #and judge_ellipse(42500, 40000, 14500, 6500, x, y, True)==True
                #and judge_ellipse(42500, 40000, 14000, 6000, x, y, False)==True
                #and judge_dir(42500, 40000, x, y, d, True)==True
                #12_out
                and judge_ellipse(42500, 40000, 14500, 6500, x, y, True)==True
                and judge_ellipse(42500, 40000, 14000, 6000, x, y, False)==True
                and judge_dir(42500, 40000, x, y, d, False)==True
                #28_in
                #and judge_ellipse(40000, 38000, 15000, 10000, x, y, True)==True
                #and judge_ellipse(40000, 38000, 14500, 9500, x, y, False)==True
                #and judge_dir(40000, 38000, x, y, d, True)==True
                and c == 2
                and v > vel
                ):
                id_list_ell.append(id)
                if len(id_list_ell) > num_id:
                    id_list_ell.pop()
                total_ell_s += 1
            """
        i = i + 1

tcm = 0
while tcm < num_gl:
    row_mat_2d[tcm].append(total_mat_1d[tcm])
    tcm += 1

total_ell_1d.append(total_ell_s)

for i in range(num_gl):
    print(str(i),":",row_mat_2d[i])
print(total_ell_1d)

with open(path+"\\res.csv","w+",newline="") as fff:
    wfdata = csv.writer(fff)
    for line in row_mat_2d:
        wfdata.writerow(line)
    #fff.writerow(total_ell_1d)

# print("Error list;",error_list)
print(datetime.datetime.fromtimestamp(firsttime),"ProgramEND")
