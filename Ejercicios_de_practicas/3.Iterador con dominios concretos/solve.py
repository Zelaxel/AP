
class My_Iterator:

    def __init__(self, digits, digits_value):
        self.__dig = digits
        self.__val = digits_value
        self.__num = []
        self.__max = []
        for i in range(self.__dig):
            self.__num.append(self.__val[i][0])
        for i in range(self.__dig):
            self.__max.append(self.__val[i][-1])
    
    def next(self):
        yield self.__num.copy()
        while self.__num != self.__max:
            self.__next()
            yield self.__num.copy()
        
    def __next(self):
        for i in range(self.__dig-1, -1, -1):
            index = self.__val[i].index(self.__num[i])
            if index < len(self.__val[i])-1:
                self.__num[i] = self.__val[i][index+1]
                break
            self.__num[i] = self.__val[i][0]