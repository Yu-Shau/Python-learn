def get_digits(x):
    """递归算法实现数值变数组"""
    
    if(x // 10 == 0):
        return [x]
    else:
        return get_digits(x // 10) + [x % 10]
