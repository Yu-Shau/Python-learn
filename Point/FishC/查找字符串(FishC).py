def findStr(desStr, subStr):
    count = 0
    length = len(desStr)
    length1 = len(subStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length - length1):      
            if desStr[each1: each1 + length1] == subStr:
                count += 1
                    
        print('子字符串在目标字符串中共出现 %d 次' % count)

desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串：')
findStr(desStr, subStr)
