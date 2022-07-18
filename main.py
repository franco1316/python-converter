from converter import Convert, ConvertToNumber, ConvertToSymbol, Random

random = Random()
number_1 = Convert(random.number, random.old_base)

symbol_1 = ConvertToSymbol(random.number, random.old_base, random.new_base)
symbol_1.convert()

print(symbol_1)