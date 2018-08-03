#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import boto3
import os
import re
import time
import sys
import csv

# csvログの保存されるディレクトリにこの.pyファイルを置いて実行してください。
# ディレクトリ内に既にログファイルがあっても大丈夫ですが、csv以外のファイルがあると不具合が発生します。
# アクセス拒否されたらいったん飛ばしますが、その後され続けたら正常に動かない気がします。
# 先にこのプログラムを稼働開始してから計測するのをおすすめします。
path = "C:\\Users\\1500570\\Documents\\R\\WS\\tesy"
#path =os.getcwd()

#差分チェック実行の概ねの周期をヘルツ単位で入力、他の処理の時間もあるので正確ではなくあくまで概ね
hlz =1

dirltemp = os.listdir(path)
datatmp =list(csv.reader(open(path +"\\" +os.listdir(path)[-1].replace("'",""), 'r+')))
tmplln =datatmp[-1]
print(tmplln)

while True:
    outp =[]
    time.sleep(float(1/hlz))
    dirl = os.listdir(path)
    sa = list(set(dirl) -set(dirltemp))
    fn = dirltemp[-1]
    try:
        data =list(csv.reader(open(path +"\\" +fn.replace("'",""), 'r+')))
        for lln in range(len(data)):
            if data[-(lln+1)] !=tmplln:
                #print(data[-(lln+1)])
                outp.append(data[-(lln+1)])
            elif len(outp) >0:
                tmplln =outp[0]
                break
            else:
                print("更新なし")
                break
    except:
        print("現行ファイルからアクセス拒否されました")
    if len(sa) == 1:
        print("sa",sa)
        dirltemp =dirl
        sys.stdout.flush()
        fn = sa[0].replace("'","")
        try:
            data =list(csv.reader(open(path +"\\" +fn, 'r+')))
            for llnn in range(len(data)):
                #print(data[-(llnn+1)])
                outp.append(data[-(llnn+1)])
        except:
            print("新ファイルを検出しましたが、アクセス拒否されました")
    #配列変数outpの中に差分が格納されているので、好きにしてください.インデックス若いほうが古いデータです
    print("更新データ数：",len(outp))

print("fin")
