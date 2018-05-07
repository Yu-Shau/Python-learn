import urllib.request
import codecs
import chardet

#   打开URL文件并获取网址信息

def get_addr(file_addr):
    url_addr = []
    with open(file_addr) as f:
        for each in f:
            url_addr.append(each)
    return url_addr


#   爬取网页信息
def spider_url(url_addr):
    html = urllib.request.urlopen(url_addr).read()
    code = chardet.detect(html)["encoding"]
    print(code)
    html = html.decode(code)
    return (html, code)

#   保存文件
def save_url(html, name, code):
    with codecs.open(r"F:\Source\Python\Point\Spider\test1\%s" % name, "w", code) as f:
        f.writelines(html)

if(__name__ == "__main__"):
    url_addr = get_addr(r"F:\Source\Python\Point\Spider\test1\urls.txt")
    for each in range(len(url_addr)):
        print(each)
        name = "url_" + str(each + 1) + ".txt"
        (html, code) = spider_url(url_addr[each])
        save_url(html, name, code)
