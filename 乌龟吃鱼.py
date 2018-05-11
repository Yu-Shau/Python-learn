#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
class Role:
    __x = 0
    __y = 0

    def __init__(self):     #随机生成位置
        self.__x = random.randint(0, 10)
        self.__y = random.randint(0, 10)

    def Move(self):     #随机进行移动
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = random.randint(0, 3)
        if(0 <= self.__x + direction[n][0] <= 10):
            self.__x += direction[n][0]
        else:
            self.__x -= direction[n][0]
        if(0 <= self.__y + direction[n][1] <= 10):
            self.__y += direction[n][1]
        else:
            self.__y -= direction[n][1]

    def Getpos(self):
        return self.__x, self.__y

class Turtle(Role):
    __live = 100

    def Getlive(self):
        return self.__live

    def Liveminus(self):
        self.__live -= 1

    def Liveplus(self):
        self.__live += 20

def main():
    t = Turtle()
    f = []
    for i in range(10):     #生成10条鱼
        temp = Role()
        if(temp.Getpos() == t.Getpos()):
            temp = Role()
        f.append(temp)
        print(f[i].Getpos())

    print("乌龟的初始位置在{}".format(t.Getpos()))
    ff = 0
    while(True):    #开始移动
        tfoo = random.randint(1, 2)     #随机乌龟移动次数(1-2)
        ff += tfoo
        while(tfoo > 0):
            tfoo -= 1
            t.Move()
            t.Liveminus()
        for each in f:      #10条鱼移动
            each.Move()

        for each in f:      #判断是否有鱼被吃
            if(t.Getpos() == each.Getpos()):
                f.remove(each)
                t.Liveplus()

        if(len(f) == 0):
            print("鱼被吃完,游戏结束!")
            break
        if(t.Getlive() <= 0):
            print("乌龟死亡,游戏结束")
            break
if __name__ == "__main__":
    main()
