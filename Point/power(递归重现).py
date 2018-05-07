def power(x, y):
    if(y == 0):
        return 1
    elif(y == 1):
        return x
    else:
        y -= 1
        return x * power(x, y)

