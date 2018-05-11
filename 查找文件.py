#!/usr/bin/python
# -*- coding: utf-8 -*-

"""查找文件"""
import os

addr = input("请输入目录:")
name = input("请输入查找的文件名:")
os.chdir(addr)

temp = list(os.walk(addr))
for i in range(len(temp) - 1):
    if(name in temp[i][2]):
        print(temp[i][0] + "\\" + name)
