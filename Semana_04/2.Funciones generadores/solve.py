# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    
    next_digits = digits.copy()
    
    for i in range(len(digits)-1, -1, -1):
        next_digits[i] += 1
        if next_digits[i] < base:
            break
        next_digits[i] = 0

    return next_digits
    
# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 2.1 Añade código aqui
        # ...
        self.__num = [0] * num_digits
        self.__base = base

    def next(self):
        # 2.2 Añade código aqui
        # ...
        for i in range(self.__base ** len(self.__num)):
            yield self.__num
            self.__num = next_number(self.__num, self.__base)
        
        # Cuando no quedan valores simplemente retornamos
        return
