import urllib.request

html = urllib.request.urlopen("http://www.fishc.com").read()
html = html.decode("utf-8")
for i in range(300):
    print(html[i], end = "")
