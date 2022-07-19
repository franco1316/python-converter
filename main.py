from converter import ConvertToNumber, ConvertToSymbol, Random

random = Random()

symbol_1 = ConvertToSymbol(random.number, random.old_base, random.new_base)

symbol_1.convert()
print(symbol_1)
print(symbol_1.get_number())
print(symbol_1.get_symbol())

try:
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.base, symbol_1.current_base)
except ValueError:
    new_base = 1
    while new_base < 2 or new_base > 10:
        print('Reinput the value of the new base between 2 - 10')
        new_base = int(input('New base: '))
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.base, new_base)


number_1.convert()
print(number_1)
print(number_1.get_symbol())
print(number_1.get_number())