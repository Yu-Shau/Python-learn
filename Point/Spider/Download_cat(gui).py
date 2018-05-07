import easygui as g
import urllib.request

msg = "下载一只喵"
title = "请填写喵的尺寸"

(width, height) = g.multenterbox(msg, title, ("宽", "高"))
save_addr = g.diropenbox()
save_addr = save_addr + "//" + width + "_" + height + ".jpg"
response = urllib.request.urlopen("http://placekitten.com/%s/%s" % (width, height))
cat_img = response.read()

with open(save_addr, "wb") as f:
    f.write(cat_img)
