import sysclass const:

    def __setattr__(self, name, value):
        try:
            if(not name.isupper()):
                raise TypeError("常量名必须由大写字母组成!")
            getattr(self, name)
            raise TypeError("常量无法改变!")
        except AttributeError:
            super().__setattr__(name, value)

sys.modules[__name__] = const()
