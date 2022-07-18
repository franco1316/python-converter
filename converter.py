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

    def __init__(self, num: int, current_base: int) -> None:
        super().__init__(num, current_base)

    def __str__(self) -> str:
        return super().__str__()


class Random():
    def __init__(self) -> None:
        self.old_base = random.randint(2, 36)
        self.new_base = random.randint(2, 36)
        self.number = random.randint(0, 80)
        
