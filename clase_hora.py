class hora():
    __hora1=None
    __min1=None
    __seg1=None
    def __init__(self,h,m,s):
        self.__hora1=h
        self.__min1=m
        self.__seg1=s
    def mo(self):
        print("--------------")
        print(self.__hora1)
        print(self.__min1)
        print(self.__seg1)
        print("--------------")
        print("|{}:{}:{}|".format(self.__hora1,self.__min1,self.__seg1))
    def gethora(self):
        return self.__hora1
    def getmin(self):
        return self.__min1
    def getseg(self):
        return self.__seg1