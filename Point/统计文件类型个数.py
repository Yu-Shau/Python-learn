"""统计目录下不同类型文件个数"""

import os
os.chdir(r"F:\Source\Python")

temp = dict()
file_list = []
file_temp = os.listdir(os.curdir)
for each in file_temp:
    file_list.append(os.path.splitext(each))
for each in file_list:
    if(each[1] not in temp):
        temp.update({each[1] : 1})
    else:
        temp[each[1]] += 1
name = temp.keys()
for each in name:
    if(each == ""):
        print("该文件夹下共有类型为[文件夹]的文件%d个" % temp[each])
    else:
        print("该文件夹下共有类型为[%s]的文件%d个" % (each, temp[each]))
