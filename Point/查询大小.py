"""查询文件夹内文件大小"""
import os
os.chdir(r"F:\Source\Python")

file_list = []
file_temp = os.listdir(os.curdir)
for each in file_temp:
    file_list.append(os.path.splitext(each))

for each in file_temp:
    if(os.path.isfile(each)):
        print(each + " [%sBytes]" % os.path.getsize(each))
