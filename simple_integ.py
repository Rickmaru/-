#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8
import re
import os
import csv
# import random

# pathへは統合したい人流csvデータ群が格納されたディレクトリのパスを入力してください。
# エクスプローラからコピーしたパスではディレクトリ間の接続が「\」で表現されていますが、これを「\\」にしてください。
# このプログラムは、入力ファイルの指定および変数f2にある出力ファイル名の指定以外、改変して利用はしません。
path = "C:\\Users\\1500570\\Documents\\R\\WS\\aogaku0130\\0130"
# datee = "161111_1718"

# [MAIN]Process to sequentially read and integrate csv stored in arr1
# seiki_fold = re.compile("\d+_\d+")
seiki_csv = re.compile("TRJ.+csv")
i = 0
firstflag = True

def extr_csv(row):
    output = seiki_csv.match(row)
    return output

# Process to append the matched csv file name path group to the arr1 list
arr1 = []
list_dir = os.listdir(path)
for row in list_dir:
    if extr_csv(row) != None:
        arr1.append(path + "\\" + extr_csv(row).group())

print(arr1)
print("Length of files list:",len(arr1))

f2 = open(path + "\\integrated_.csv", "w+", newline="")
datawriter = csv.writer(f2)
datawriter.writerow(["unixtime","id","x","y","z","velocity","direction","acceleration","ang_velocity","category","grid_id","area_id","size"])

ff = True

# main():
while i < len(arr1):
    print(i,"/",len(arr1),"is starting")
    f1 = open(arr1[i],"r")
    datareader = csv.reader(f1)
    # Subscript partial counted
    for line in datareader:
        del line[13]
        # cat = float(line[9])
        # vel = float(line[5])
        # if random.random() > -1:
        #     if cat == 2 and vel >= 0.5:
        datawriter.writerow(line)
    i = i + 1
    f1.close()
f2.close()

print("ProgramEND")
