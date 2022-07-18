import math
import random
from colors import Colors

class Convert:
    def __init__(self, num: int, old_base: int) -> None:
        self.__old_num = num
        self.__old_base = 10
        self.__DICTIONARY = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__basic_dictionary = '0123456789'
        self.num = 0
        self.base = old_base

    def get_dictionary(self) -> str:
        return self.__DICTIONARY

    def get_basic_dictionary(self) -> str:
        return self.__basic_dictionary

    def set_basic_dictionary(self, value: str) -> None:
        self.__basic_dictionary = value

    def get_old_num(self) -> str:
        return self.__old_num

    def set_old_number(self, value: str) -> None:
        self.__old_num = value

    def get_old_base(self) -> int:
        return self.__old_base

    def set_old_base(self, value: int) -> None:
        self.__old_base = value

    def set_num(self, value: str) -> None:
        self.num = value

    def get_base(self) -> None:
        return self.base 

    def set_new_base(self, value: int) -> None:
        self.base = value

    def __str__(self) -> str:
        my_colors = Colors()
        return (f'{my_colors.GREEN}{self.__old_num}{my_colors.MAGENTA}({self.__old_base}){my_colors.DEFAULT} => '
        f'{my_colors.GREEN}{self.num}{my_colors.MAGENTA}({self.base}){my_colors.DEFAULT}\n')

        

        
class ConvertToSymbol(Convert):
    def __init__(self, num: int, old_base: int, current_base: int) -> None:
        super().__init__(num, old_base)
        self.current_base = current_base

    
    def convert(self) -> None:
        number = self.get_old_num()
        base = self.get_base()
        dictionary = self.get_dictionary()
        self.set_basic_dictionary(dictionary[0 : base])
        my_dictionary = self.get_basic_dictionary()
        symbol = ''
        temporal_number = number
        while temporal_number >= base:
            rest = temporal_number % base
            temporal_number //= base
            symbol += my_dictionary[rest]
        symbol += my_dictionary[temporal_number]
        symbol = symbol[::-1]
        self.set_num(symbol)


    def __str__(self) -> str:
        return super().__str__()




class ConvertToNumber(Convert):

    def __init__(self, num: int, old_base: int, current_base: int) -> None:
        if old_base>current_base:
            super().__init__(num, old_base)
            self.current_base = current_base
        else: 
            raise ValueError('The new base must be between the 2 - 10')

    def convert(self) -> None:
        symbol = str(super().get_old_num())
        base = self.base
        new_base = self.current_base
        dictionary = self.get_dictionary()
        self.set_basic_dictionary(dictionary[0 : base])
        my_dictionary = self.get_basic_dictionary()
        new_dictionary = self.get_basic_dictionary()[0 : new_base]
        num = self.__x_to_10(symbol, base, my_dictionary)
        new_num = self.__10_to_y(num, new_base, new_dictionary)
        self.set_num(new_num)
        super().set_old_base(self.base)
        super().set_new_base(self.current_base)

    def __x_to_10(self, num: str, base: int, dictionary: str) -> int:
        num = num[::-1]
        index = 0
        number = 0
        sum = 0
        aditional = 0
        while index < len(num):
            symbol = num[index]
            index_dictionary = dictionary.find(symbol)
            if index_dictionary > 9:
                rest = index_dictionary % 10
                aditional = index_dictionary - rest
                index_dictionary = rest + aditional
            number = int(index_dictionary) * int((math.pow(base, index)))#i*n(i)
            sum += number 
            print(f'{base}(e{index}) = {int((math.pow(base, index)))} * number = {index_dictionary} = {number}')
            index += 1

        return sum

    def __10_to_y(self, num: int, new_base: int, new_dictionary: str) -> int:
        number = ''
        temporal_number = num
        while temporal_number >= new_base:
            rest = temporal_number % new_base
            temporal_number //= new_base
            number += new_dictionary[rest]
        number += new_dictionary[temporal_number]
        number = number[::-1]
    
        return number
        

    def __str__(self) -> str:
        return super().__str__()


class Random():
    def __init__(self) -> None:
        self.old_base = random.randint(2, 36)
        self.new_base = random.randint(2, 36)
        self.number = random.randint(0, 80)
