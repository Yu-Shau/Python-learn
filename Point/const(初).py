import sys
class const:
    def __init__(self, name, value):
        if(name.isupper()):
            super().__setattr__(name, value)
        else:
            raise TypeError("常量名必须由大写字母组成!")

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        try:
            if(not name.isupper()):
                raise TypeError("常量名必须由大写字母组成!")
            getattr(self, name)
            raise TypeError("常量无法改变!")
        except AttributeError:
            super().__setattr__(name, value)

sys.modules[__name__] = const("N", "N")     #会有一个const.N不知道怎么删除
