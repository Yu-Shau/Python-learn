import easygui as g

def new_data(name, num):
    data[name] = num
    return 1

def load(name, num):
    if(data[name] == num):
        return 1
    else:
        return 0


print("""
|--- 新建用户: N/n ---|
|--- 登录账号: E/e ---|
|--- 退出程序: Q/q ---|""")
data = {}

while(True):
    flag = 0
    code = input("|--- 请输入指令代码:")

    if(code == "N" or code == "n"):
        name = input("请输入用户名:")
        while(name in data):
            if(flag > 2):
                break
            name = input("此用户名已经被使用,请重新输入:")
            flag += 1
        if(flag == 3):
            continue
        num = input("请输入密码:")
        if(new_data(name, num)):
            print("注册成功,赶紧试试登录吧^_^")
        else:
            print("注册失败,请重新注册!")

    if(code == "E" or code == "e"):
        name = input("请输入用户名:")
        while(name not in data):
            if(flag > 2):
                break
            name = input("您输入的用户名不存在,请重新输入:")
            flag += 1
        if(flag == 3):
            continue
        num = input("请输入密码:")
        if(load(name, num)):
            g.msgbox("欢迎进入XXOO系统,请点击右上角的X退出程序!")
        else:
            print("用户名,密码不正确!")

    if(code == "Q" or code == "q"):
        break

