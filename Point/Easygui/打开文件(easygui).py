import easygui as g
import os

temp_old = ""
choice = g.buttonbox(choices = ["打开文件", "退出"])
if(choice == "打开文件"):
    addr_open = g.fileopenbox()
msg = "文件[%s]的内容如下:" % os.path.split(addr_open)[1]
title = "显示文件内容"
with open(addr_open) as f:
    for each in f:
        temp_old += each
temp_new = g.textbox(msg, title, temp_old, codebox = True)

if(temp_new != temp_old):
    b = g.buttonbox(msg = "检测到文件内容发生改变,请选择以下操作:", title = "警告",
               choices = ["覆盖保存", "放弃保存", "另存为"])
    if(b == "覆盖保存"):
        with open(addr_open, "w") as f:
            f.writelines(temp_new)
    if(b == "另存为"):
        addr_new = g.filesavebox()
        with open(addr_new, "w") as f:
            f.writelines(temp_new)
