from urllib.request import Request, urlopen
from urllib.error import URLError

req = Request("http://www.fishc.com/ooxx.html")
try:
    res = urlopen(req)
except URLError as e:
    if hasattr(e, "reason"):
        print("We failed to reach a server.")
        print("Reason:", e.reason)
    elif hasattr(e, "code"):
        print("The server couldn\'t fulfill the request.")
        print("Error code:", e.code)
else:
    #everything is fine
    pass

"""
try:
    res = urlopen(req)
except HTTPError as e:
    print("The server couldn\'t fulfill the request.")
    print("Error code:", e.code)
except URLError as e:
    print("We failed to reach a server.")
    print("Reason:", e.reason)
else:
    #everything is fine
    pass
"""
