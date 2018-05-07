def my_fun(x):
    """递归判断是不是回文"""

    if(len(x) <= 1):
        return "是回文"
    elif(x[0] == x[-1]):
        return my_fun(x[1: -1])
    else:
        return "不是回文"
