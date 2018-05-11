#!/usr/bin/python
# -*- coding: utf-8 -*-

"""查找文件夹中所有指定类型文件"""
import os

addr = input("请输入目录:")
data = [".avi", ".mp4", ".rmvb", ".mkv"]
f = open(r"F:\Source\Python\result.txt", "w")
addr_data = []
os.chdir(addr)

temp = list(os.walk(addr))
for i in range(len(temp)):
    for each in temp[i][2]:
        name =str(temp[0][0]) + "\\" + str(each)
        if(os.path.splitext(name)[1] in data):
            f.writelines(name + "\n")

f.close()
