#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

import boto3
import os
import re
import time
import sys
from uhurusys_json_trans import main_jsontrans

seiki_csv = re.compile("TRJ.+csv")

# pathは人流csvデータが保存されるディレクトリのパス、jpathはuhuruシステム用のjsonを掃出したいディレクトリのパスを指定してください。
# エクスプローラからコピーしたパスではディレクトリ間の接続が「\」で表現されていますが、これを「\\」にしてください。
# このプログラムを稼働させている間、常に最新の人流csvデータおよびjsonファイルをAWSへアップロード・更新し続けます。
# jsonファイルの自動更新を止めたい場合、以下に指示が書いてありますのでそれに従ってください。
# jsonの自動更新のために、このプログラムは別のuhurusys_json_trans.pyが必要になりますので、
# 当プログラムとuhurusys_json_trans.pyは同じディレクトリ内に保存するようにしてください。
path = "C:\\Program Files\\LaserRadar\\LOG\\CsvLog\\TRJ(ActCtl)"
pathj = 'C:\Program Files\LaserRadar\LOG\\CsvLog'

s3 = boto3.resource('s3')

i = 0
while True:
    dirl = os.listdir(path)
    time.sleep(1)
    dirltemp = os.listdir(path)
    sa = list(set(dirltemp) -set(dirl))
    if len(sa) == 1:
        sys.stdout.write("\ryes")
        sys.stdout.flush()
        fn = dirl[-1]
        print(path +"\\" +fn.replace("'",""))
        data = open(path +"\\" +fn.replace("'",""), 'rb')
        # ここでバケット名、ディレクトリパスを入力すると任意の自動アップロード場所を指定できます。
        s3.Bucket('yahoo.lodge').put_object(Key='rowdata/'+fn, Body=data)
        data.close()
        # jsonアップロードを止める場合、↓をコメントアウトしてください
        main_jsontrans(fn,path,pathj)
        dataj = open(pathj +"\\" +"trajects.json", 'rb')
        # ここでバケット名、ディレクトリパスを入力すると任意の自動アップロード場所を指定できます。
        s3.Bucket('yahoo.lodge').put_object(Key='statics/trajects.json', Body=dataj)
        dataj.close()
        # jsonアップロードを止める場合、↑をコメントアウトしてください
    else:
        i +=1
        sys.stdout.write("\r %d" %i)
        sys.stdout.flush()
print("fin")
