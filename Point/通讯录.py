print("""
|---欢迎进入通讯录程序---|
|---1: 查询联系人资料 ---|
|---2: 插入新的联系人 ---|
|---3: 删除已有联系人 ---|
|---4: 退出通讯录程序 ---|""")

data_dict = dict()
flag = 0

while(flag != 4):
    num = name = ""
    flag = 0
    flag = int(input("请输入相关的指令代码:"))
    
    if(flag == 1):
        name = input("请输入联系人姓名:")
        if(data_dict.get(name) == None):
            print("此联系人不存在!")
        else:
            print(name + " : " + data_dict.get(name))
    elif(flag == 2):
        name = input("请输入联系人姓名:")
        if(data_dict.get(name) == None):
            num = input("请输入用户联系电话:")
            data_dict.update({name: num})
        else:
            print("您输入的姓名在通讯录中已存在 -->>%s : %s" %(
                name, data_dict.get(name)))
            if(input("是否修改用户资料(YES/No)") == "YES"):
                num = input("请输入用户联系电话:")
                data_dict.update({name: num})
    elif(flag == 3):
        name = input("请输入联系人姓名:")
        if(data_dict.get(name) == None):
            print("此联系人不存在!")
        else:
            data_dict.pop(name)


print("|--- 感谢使用通讯录程序 ---|")
