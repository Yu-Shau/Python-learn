import os
import easygui as g

code_type = [".py", ".c", ".asm", ".cpp", ",pas", ".m", ".html"]
data = {".py":[0, 0], ".c":[0, 0], ".cpp":[0, 0], ".asm":[0, 0], ".pas":[0, 0], ".m":[0, 0], ".html":[0, 0]}

def count_lines(file_temp):
    count = 0
    with open(file_temp, "rb") as f:
        for i in f:
            count += 1
    return count
        
def find_code(addr):
    temp = os.listdir(addr)
    for each in temp:
        if(os.path.isfile(addr + "\\" + each)):
            suff = os.path.splitext(each)[1]
            if(suff in code_type):
                data[suff][0] += count_lines(addr + "\\" + each)
                data[suff][1] += 1
        else:
            find_code(addr + "\\" + each)

addr = g.diropenbox()
find_code(addr)
total_lines = 0
for each in data:
    total_lines += data[each][0]
temp = ""
msg = "您目前共累积编写了%d行代码,完成进度%.2f%%\n离10万行代码还差%d行,请继续努力!" %(
    total_lines, total_lines / 100000 * 100, 100000 - total_lines)
for each in data:
    temp += ("[%s]源文件%d个,源代码%d行" % (each, data[each][1], data[each][0])
                + "\n")
g.textbox(msg, "统计结果", temp)
