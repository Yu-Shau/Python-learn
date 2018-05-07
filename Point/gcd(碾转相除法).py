def gcd(x, y):
    temp = x % y
    if(temp == 0):
        return y
    else:
        return gcd(y,temp)