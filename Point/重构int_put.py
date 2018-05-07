def int_input(char = ""):
    while True:
        try:
            temp = int(input())
            break
        except ValueError:
            print("Error:请输入整数!")
    return temp
