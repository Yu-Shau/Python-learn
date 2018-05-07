def new_bin(x):
    """递归实现十进制转二进制"""
    
    if(x == 0):
        return "0b0"
    elif(x == 1):
        return "0b1"
    else:
        return new_bin(x // 2) + str(x % 2)
