from converter import Convert, ConvertToNumber, ConvertToSymbol, Random

random = Random()
convert_1 = Convert(random.number, random.old_base)

symbol_1 = ConvertToSymbol(random.number, random.old_base, random.new_base)
symbol_1.convert()

try:
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.base, symbol_1.current_base)
except ValueError:
    new_base = 1
    while new_base < 2 or new_base > 10:
        print('Reinput the value of the new base between 2 - 10')
        new_base = int(input('New base: '))
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.base, new_base)
else:
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.base, symbol_1.current_base)

number_1.convert()


print(symbol_1)
print(number_1)


# convert_1 = Convert(23, 26)

# symbol_1 = ConvertToSymbol(23, 26, 10)
# symbol_1.convert()

# number_1 = ConvertToNumber(symbol_1.num, symbol_1.base, 4)
# number_1.convert()


# print(symbol_1)
# print(number_1)