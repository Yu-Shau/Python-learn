print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    try:
        instr = int(input('\n请输入相关的指令代码：'))
        
        if instr == 1:
            name = input('请输入联系人姓名：')
            print(name + ' : ' + contacts[name])

        if instr == 2:
            name = input('请输入联系人姓名：')
            if name in contacts:
                print('您输入的姓名在通讯录中已存在 -->> ', end='')
                print(name + ' : ' + contacts[name])
                if input('是否修改用户资料（YES/NO）：') == 'YES':
                    contacts[name] = input('请输入用户联系电话：')
            else:
                contacts[name] = input('请输入用户联系电话：')

        if instr == 3:
            name = input('请输入联系人姓名：')
            del(contacts[name])         # 也可以使用dict.pop()
                
        if instr == 4:
            break
    except KeyError as reason:
        print("您输入的联系人不存在" + str(reason))

print('|--- 感谢使用通讯录程序 ---|')
