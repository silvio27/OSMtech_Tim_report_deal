
# -*- coding: utf-8 -*-
import os
import re

def rename_001(path,folder):
    path1 = path
    path = path + folder +'/'
    f = os.listdir(path)
    n = 0
    j = []
    for i in f:
        j.append(i)
        if n >= 99:
            newname = folder + str(n + 1) + ".jpg"
        elif n >= 9:
            newname = folder + '0' + str(n + 1) + ".jpg"
        elif n >= 0:
            newname = folder + '00' + str(n + 1) + ".jpg"
        else:
            print('error')

        os.renames(path+f[n], path+newname)
        #将文件路径导出到dir
        add_file_path(path1, 'dir', path+newname + '\t'+ newname)

        n += 1
    print('ALL ' + str(n) + ' Done')
    print(j)


def all_folder_rename_001(path):

    path = path.replace('\\','/')
    path = path + '/'
    f = os.listdir(path)
    j = []
    for i in f:
        j.append(i)
        print(i)
    print(j)
    for n in j:
        folder = n
        rename_001(path, folder)

def add_file_path(path, filename, content):
    #可以增加判断是追加还是重新写入
    fo = open(path + filename + ".txt", "a+")
    fo.write(content + '\n')
    fo.close()



if __name__=="__main__":
    path = r'C:\Users\Silvio\Desktop\四川省成都市青白江区2019-SC-024\待整理'
    #path1 = r'C:/Users/Silvio/Desktop/四川省成都市青白江区2019-SC-024/'
    all_folder_rename_001(path)


