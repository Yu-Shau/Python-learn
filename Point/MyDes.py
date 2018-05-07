class MyDes:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        
    def __get__(self, instance, owner):
        print("正在获取变量:%s" % self.name)
        return self.value

    def __set__(self, instance, value):
        print("正在修改变量:%s" % self.name)
        self.value = value

    def __delete__(self, instance):
        print("正在删除变量:%s" % self.name)
        print("哦~这个变量没法删除~")
