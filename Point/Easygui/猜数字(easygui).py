import random
import easygui as g

secret = random.randint(1, 10)
count = 3
title = "数字小游戏"
msg = "不妨猜一个数字(1~10):"
while count > 0:
    result = int(g.enterbox(msg, title))
    if(result == secret):
        g.msgbox("You Win!")
        break
    elif(result > secret):
        g.msgbox("大了!还有%d次机会" % (count - 1))
    elif(result < secret):
        g.msgbox("小了!还有%d次机会" % (count - 1))
    else:
        g.msgbox("Wrong!")
    count -= 1
