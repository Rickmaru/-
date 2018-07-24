#author:R.Kunimoto, TAKENAKA co.
#coding:utf-8
import os
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import copy
import networkx as nex
from scipy.spatial.distance import cityblock
from scipy.spatial import distance

plt.close()
path = 'C:\\Users\\1500570\\Documents\\R\\WS\\dataset_a4\\unchi'

arr1 = os.listdir(path)
print("Length of files list:",len(arr1))
# print(arr1)

wx =300
wy =300
bord = 0.2

n_dm =[]
n_ds =[]
def count_weight(x,y):
    global df
    global n_dm
    global n_ds
    global wx
    global wy
    tmp_winf =df[df[:,2] >= x-wx]
    tmp_winf =tmp_winf[tmp_winf[:,2] <= x+wx]
    tmp_winf =tmp_winf[tmp_winf[:,3] >= y-wy]
    tmp_winf =tmp_winf[tmp_winf[:,3] <= y+wy]
    s_move =len(tmp_winf[tmp_winf[:,9] == 2.0])
    s_stay =len(tmp_winf[tmp_winf[:,9] == 1.0])
    if 0.8*s_move>s_stay:
        n_dm.append(s_move)
        return s_move
    elif 0.8*s_move<s_stay:
        n_ds.append(s_stay)
        return -s_stay
    else:
        return 0

clus_n =1
def cluster_stay(x,y):
    global clus_mat
    global eva_zero
    global clus_n
    if eva_zero[y,x] == -1:
        if x !=0 and y !=0:
            if clus_mat[y-1,x] ==0 and clus_mat[y,x-1] ==0:
                clus_mat[y,x] =clus_n
                clus_n +=1
            elif clus_mat[y-1,x] !=0:
                if clus_mat[y,x-1] !=0:
                    if clus_mat[y-1,x] !=clus_mat[y,x-1]:
                        clus_mat[y,x-1] =copy.deepcopy(clus_mat[y-1,x])
                        ift =1
                        while True:
                            if clus_mat[y,x-(ift+1)] !=0 and clus_mat[y,x-(ift+1)] !=clus_mat[y,x-ift]:
                                clus_mat[y,x-(ift+1)] =copy.deepcopy(clus_mat[y,x-ift])
                                ift +=1
                            else:
                                break
                    clus_mat[y,x] =copy.deepcopy(clus_mat[y,x-1])
                clus_mat[y,x] =copy.deepcopy(clus_mat[y-1,x])
            elif clus_mat[y,x-1] !=0:
                clus_mat[y,x] =copy.deepcopy(clus_mat[y,x-1])
            else:
                print("へにょ")
        elif x ==0:
            if clus_mat[y-1,x] ==0:
                clus_mat[y,x] =clus_n
                clus_n +=1
            elif clus_mat[y-1,x] !=0:
                clus_mat[y,x] =copy.deepcopy(clus_mat[y-1,x])
            else:
                print("なんかへにょ")
        elif y ==0:
            if clus_mat[y,x-1] ==0:
                clus_mat[y,x] =clus_n
                clus_n +=1
            elif clus_mat[y-1,x] !=0:
                clus_mat[y,x] =copy.deepcopy(clus_mat[y-1,x])
            else:
                print("なんかへに")
        else:
            print("うんち")

i=0
while i < len(arr1):
    with open(path +"\\" +arr1[i],"r") as f1:
        a =np.array(list(csv.reader(f1)))[:,0:10].astype(np.float64())
        print(i+1,"/",len(arr1),"th file is starting, length", len(a),type(a))
        if i == 0:
            df =a
        else:
            df=np.vstack((df,a))
        print("integrated size=", len(df))
        """
        for line in datareader:
            # Need more strict condition?
            # if len(line)==24 or len(line)==14:
            time = float(line[0])
            id = float(line[1])
            x = float(line[2])
            y = float(line[3])
            velocity = float(line[5])
            direction = float(line[6])
            category = int(line[9])
        """
    i += 1
df =np.array(sorted(df, key=lambda x:(float(x[2]),float(x[3])), reverse=False))
ylen =int(max(df[:,3])-min(df[:,3]))+1
xlen =int(max(df[:,2])-min(df[:,2]))+1

eva_zero =np.zeros((int(ylen/wy)+2,int(xlen/wx)+2))

i2 =0
print(ylen,xlen)
while i2 <ylen:
    print(i2,"/",ylen)
    i3 =0
    while i3 <xlen:
        eva_zero[-int(i2/wy),int(i3/wx)] =count_weight(i3, i2)
        i3 +=wx
    i2 +=wy

n_dm =sorted(n_dm)
n_ds =sorted(n_ds)

i4 =0
while i4<len(eva_zero):
    i5 =0
    if i4%10 ==0:
        print("i4=",i4,"/",len(eva_zero))
    while i5<len(eva_zero[i4]):
        if eva_zero[i4,i5] > n_dm[int(len(n_dm)*0.01)]:
            eva_zero[i4,i5] =1
        elif eva_zero[i4,i5] < -n_ds[int(len(n_ds)*0.6)]:
            eva_zero[i4,i5] =-1
        else:
            eva_zero[i4,i5] =0
        i5 +=1
    i4 +=1

clus_mat =np.zeros((len(eva_zero),len(eva_zero[0])))

i6 =0
while i6<len(clus_mat):
    i7 =0
    while i7<len(clus_mat[i6]):
        cluster_stay(i7, i6)
        i7 +=1
    i6 +=1

clus_cordi =[]
p =1
while p <=clus_n:
    matched =np.where(clus_mat ==p)
    if len(matched[0]) !=0:
        clus_cordi.append([int((max(matched[0]) +min(matched[0]))/2), int((max(matched[1]) +min(matched[1]))/2)])
    #else:
        #clus_cordi.append(False)
    p +=1

#clus_cordi.append([max(matched[0,:])-min(matched[0,:]), max(matched[1,:])-min(matched[1,:])])
plt.show(sns.heatmap(eva_zero))
plt.show(sns.heatmap(clus_mat,cmap="jet"))
print(clus_cordi)

dist_mat =distance.cdist(clus_cordi,clus_cordi, metric ='mahalanobis')
print(dist_mat)
dist_mat2 =np.reshape(dist_mat,len(dist_mat)**2)
dist_mat2 =dist_mat2[dist_mat2 !=0]
kijun =int((max(dist_mat2) +min(dist_mat2))/2)
print(kijun)
gg =nex.Graph()

pp =0
pos ={}
while pp <len(clus_cordi):
    gg.add_node("node"+str(pp))
    pos["node"+str(pp)] =[clus_cordi[pp][1],-clus_cordi[pp][0]]
    pp +=1

a1 =0
dist_mat =[]
while a1<len(clus_cordi):
    a2 =copy.deepcopy(a1)
    while a2<len(clus_cordi):
        if a2 ==a1:
            a2 +=1
            continue
        elif int(cityblock(clus_cordi[a1],clus_cordi[a2])) <20:
            gg.add_edge("node"+str(a1), "node"+str(a2))
        a2 +=1
    a1 +=1

nex.draw(gg, pos)
plt.show()

print("end")

"""
df =np.array(sorted(list(datareader), key=lambda x:(float(x[2]),float(x[3])), reverse=False))[:,0:10].astype(np.float64)
x_max =max(df[:,2])
x_min =min(df[:,2])
y_max =max(df[:,3])
y_min =min(df[:,3])
eva_zero =np.zeros()
xi =0
yi =0
while yi <max(df[:,3]):
    while xi <max(df[:,2]):
        # ウィンドウをwinfへ格納
        winf =df[df[:,2]>xi]
        winf =winf[winf[:,2]<xi+window_sizex]
        winf =winf[winf[:,3]>yi]
        winf =winf[winf[:,3]<yi+window_sizey]
        arr_move.append(winf[:,9])
        arr_stay.append(winf[:,9])
        # ヒストグラム描写
"""