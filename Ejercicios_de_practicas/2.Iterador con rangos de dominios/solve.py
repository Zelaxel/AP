
class My_Iterator:

    def __init__(self, digits, min_value, max_value):
        self.__dig = digits
        self.__min = min_value
        self.__max = max_value
        self.__num = min_value.copy()
    
    def next(self):
        yield(self.__num.copy())
        while self.__num != self.__max:
            self.__next_num()
            yield(self.__num.copy())

    def __next_num(self):
        for i in range(self.__dig-1, -1, -1):
            self.__num[i] += 1
            if self.__num[i] <= self.__max[i]:
                break
            self.__num[i] = self.__min[i]
    