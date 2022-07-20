from converter import ConvertToNumber, ConvertToSymbol, Random

random = Random()

symbol_1 = ConvertToSymbol(random.number, random.old_base, random.new_base)

symbol_1.convert()
print(symbol_1, symbol_1.number, symbol_1.symbol)

try:
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.new_base, symbol_1.current_base)
except ValueError:
    new_base = 1
    while new_base < 2 or new_base > 10:
        print('Reinput the value of the new base between 2 - 10')
        new_base = int(input('New base: '))
    number_1 = ConvertToNumber(symbol_1.num, symbol_1.new_base, new_base)


number_1.convert()
print(number_1, number_1.symbol, number_1.number)

print('\n\n')

#* test something crazy look at this:
random2 = Random()
num = random2.number
base = random2.old_base
new_base = random2.new_base

number_2 = ConvertToNumber(num, base, new_base)
#I can use all out of the structure of the class and use it completly free

dictionary = number_2.dictionary
dictionary_base = dictionary[0: base]
converter_x_to_10 = number_2.bx_to_10
converter_10_to_x = number_2.b10_to_y

print(num, f'({base})')

num_to_10 = converter_x_to_10(str(num), base, dictionary_base)
print(num_to_10, '(10)')

new_dictionary = dictionary[0: new_base]
num_to_new_base = converter_10_to_x(num_to_10, new_base, new_dictionary)

print(num_to_new_base, f'({new_base})')

print('\n\n')

print(number_2, 'Inside of the class has no changes, just only create an instance')





