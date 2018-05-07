import math
def myPri(index):
    for each in range(index + 1):
        if(is_prime(each)):
            yield each

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for each in range(3, int(math.sqrt(number) + 1), 2):
            if number % each == 0:
                return False
        return True
    return False
