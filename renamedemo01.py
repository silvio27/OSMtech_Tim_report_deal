
# -*- coding: utf-8 -*-
import os
import re

def rename_001(path,folder):

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



if __name__=="__main__":
    path = r'C:\Users\Silvio\Desktop\四川省成都市青白江区2019-SC-024\待整理2'
    all_folder_rename_001(path)

