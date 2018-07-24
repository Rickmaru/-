#author;R.Kunimoto, TAKENAKA co.
#coding:utf-8

# filenに変換したい人流csvデータのファイル名、pathにそのファイルが入っているディレクトリパスを指定してください。
# エクスプローラからコピーしたパスではディレクトリ間の接続が「\」で表現されていますが、これを「\\」にしてください。
# このプログラムは、入力ファイルの指定およびソースコード最下部付近にある出力ファイル名の指定以外、改変して利用はしません。
def main_jsontrans(ffnn,papath,pathj):
    import csv

    def trans(time,x,y,):
        return "{\"i\": "+str(time)+", \"v\": {\"x\": "+str(x)+", \"y\": "+str(y)+"}}"

    filen = ffnn
    print(filen)

    reader = csv.reader(open(papath+"\\"+filen,"r"))
    temp_id= []
    temp_ut= []
    temp_x= []
    temp_y= []

    for line in reader:
        temp_id.append(line[1].replace(" ",""))
        temp_ut.append(float(line[0]))
        temp_x.append(int(line[2]))
        temp_y.append(int(line[3]))

    id_list =list(set(temp_id))
    ut_list =sorted(list(set(temp_ut)))
    ini_list= [["null" for i in range(len(id_list))] for j in range(len(ut_list))]

    k=0
    while k < len(temp_id):
        ini_list[ut_list.index(temp_ut[k])][id_list.index(temp_id[k])] =[temp_x[k],temp_y[k]]
        k += 1

    sen ="[\n"

    l =0
    while l < len(id_list):
        sen += "{\n\"id\": " +str(id_list[l]) +",\n\"points\": [\n"
        m =0
        print("step:",l+1,"/",len(id_list))
        while m <len(ut_list):
            if ini_list[m][l] != "null":
                sen +=trans(ut_list[m],ini_list[m][l][0],ini_list[m][l][1]) +",\n"
            else:
                sen += "{\"i\": "+str(ut_list[m])+", \"v\": null}" +",\n"
            m +=1
            if m ==len(ut_list):
                sen =sen.rstrip(",\n\n")
                sen +="\n]\n"
        l +=1
        if l == len(id_list):
            sen +="}\n"
        else:
            sen +="},\n"
    sen.rstrip()
    sen.rstrip()
    sen +="]"

    f = open(pathj +'\\trajects.json', 'w')
    f.write(sen)
    f.close()

# main_jsontrans("")
print("finished")