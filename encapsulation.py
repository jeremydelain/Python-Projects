#class with a protected and private var
class Protected:
    def __init__(self):
        self._protectedVar = 1
        self.__privateVar = 2

#creating an istace of Protected
obj = Protected()
