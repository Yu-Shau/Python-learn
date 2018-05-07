import urllib.request
import chardet

addr = input("请输入URL:")
response = urllib.request.urlopen(addr)
html = response.read()
temp = chardet.detect(html)
print("该网页使用的编码时:%s" % temp["encoding"])
