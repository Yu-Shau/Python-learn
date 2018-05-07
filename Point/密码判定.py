symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>''' # 有点不明白小甲鱼用了三引号以后为什么还用 r？
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
length_q = 0
zuhe = 0
class1 = '您的密码安全级别评定为：低'
class2 = '您的密码安全级别评定为：中'
class3 = '您的密码安全级别评定为：高'
improve = '请按以下方式提升您的密码安全级别：\n 1.密码必须由数字、字母及特殊字符三种组合\n 2.密码只能由字母开头\n 3.密码长度不能低于16位'


temp = input('请输入需要检查的密码组合：')
length = len(temp)

while (temp.isspace() or length == 0):
    temp = input('您输入的密码为空（或空格），请重新输入：')
    length = len(temp)
    
if length <= 8:
    length_q = 1
if 8 < length <= 16:
    length_q = 2
if length > 16:
    length_q = 3
       
for each in temp:
    if each in nums:
        zuhe += 1
        break
for each in temp:    
    if each in chars:
        zuhe += 1
        break
for each in temp:
    if each in symbols:
        zuhe += 1
        break

while True:
    if zuhe == 1 and length_q == 1:
        print(class1)
        print(improve)
        break
    elif zuhe == 3 and length_q == 3 and (temp[0] in chars):
        print(class3)
        print('请继续保持')
        break
    else:
        print(class2)
        print(improve)
        break
