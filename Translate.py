#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import json
import time
import random
import hashlib
import urllib.parse
while True:
    text = input("请输入带翻译内容(输入'q!'退出程序):")
    if(text == "q!"):
        break
    
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    # 添加个人信息,防止被屏蔽
    headers = {
        "Cookie": "OUTFOX_SEARCH_USER_ID=-194811476@10.168.8.76",
        "Referer": "http://fanyi.youdao.com/?keyfrom=fanyi-new.logo",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        }
    data = {}

    # 对加密数据进行解密
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = "ebSeFb%=XZ%T[KZ)c(sy!"
    g = hashlib.md5(("fanyideskweb" + text + f + c).encode("utf-8")).hexdigest()
    data["i"] = text
    data["from"] = "AUTO"
    data["to"] = "AUTO"
    data["smartresult"] = "dict"
    data["client"] = "fanyideskweb"
    data["salt"] = f
    data["sign"] = g
    data["doctype"] = "json"
    data["version"] = "2.1"
    data["keyfrom"] = "fanyi.web"
    data["action"] = "FY_BY_REALTIME"
    data["typoResult"]: "false"

    data = urllib.parse.urlencode(data).encode("utf-8")

    # 添加header
    req = urllib.request.Request(url, data, headers)
    #req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")

    print(json.loads(html)["translateResult"][0][0]["tgt"])
    time.sleep(3)       #休眠3s进行下一次翻译

