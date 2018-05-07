class C2F(float):
    def __new__(cls, centi):
        fah = centi * 1.8 + 32
        return float.__new__(cls, fah)
