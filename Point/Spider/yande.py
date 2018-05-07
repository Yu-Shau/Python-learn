import urllib.request
import re

def open_url(url):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({'http':'115.223.198.130:9000'}))
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")]

    response = urllib.request.urlopen(url).read()
    return response

def get_imag(html):
    pat = r'<img src="([^"]+\.jpg)"'
    imag = re.findall(pat, html)

    for each in imag:        
        filename = each.split("/")[-1]
        with open(r"C:\Users\LLJY\Desktop\spider\new\%s" % filename, "wb") as f:
            ht = open_url(each)
            f.write(ht)

        
def main():
#    url = "https://yande.re/post"
    url = "http://www.facets.la/"
    html = open_url(url).decode("utf-8")
    get_imag(html)

if __name__ == "__main__":
    main()
