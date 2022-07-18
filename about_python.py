from colors import Colors
#from x import y 
#*basically meaning that from some place search and give me something


def function() -> None:
    return

def function():
    pass

# all that this both doing is return none
# when you write and the language wait another line then you can write pass:
    # pass is a statement for avoid an error
# and if the function doesn't return nothing:
    # return None by default

class Tutorial:
    def __init__(self) -> None:
        self.__variable = 'Hello world'

        #self = is the this on python is mandotory in functions that live inside of a class
        #?__init is the constructor in python

    def my_function(self, message: str or int):
        print(f'{self.__variable} and today we\'ll see {message}')

        # is opcional and a good practice put the type even if the type is none you should put for follow
        # the good practices and the conventions you manage snake case except in the class names
        # None you remember it as a void, in python all is public, the unique form to simulate private things is __ in the beggining

    @property #getter
    def another_function(self) -> str:
        return self.__variable

class Son(Tutorial):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        # return 'is that you kwnon as override look the result of call an instance of son in print'
        return f'{super().another_function} I\'m the __str__ method'

    #super() is for access at the propertys and variables of the father class

color_print = Colors().TURQOISE
color_variable = Colors().YELLOW
color_invalid = Colors().RED
color_default = Colors().DEFAULT

print(color_print)

tuto = Tutorial()
hola = 'my message' # variable creation and asignament in python
tuto.my_function(hola)
tuto.my_function(message=hola)
print('line 57', color_variable)
print('line 58', tuto._Tutorial__variable)#the formula is _ClassName__variable
#*if you want see it just only do print(tuto.__dict__)
print('line 60', tuto.another_function)
#!print(tuto.__variable) that's wrong beacuse is simulating a private variable and you dont have access

ZERO = 0 #? convencionally the constant are writting all in uppercase

son = Son()
print(color_invalid) #invalid doesn´t the best name in this case just only want the color
print('line 67' ,tuto, 'I\'m without the __str__')
print(color_print)
print('line 70' ,son)

print(color_default)

"""
Aditionaly my professor was talking ant teaching the basic of solid principles
in fact, more specifcly about the class just only change for a unique thing, Not multiple or some, just one
and always remind us that we should learning about desing patterns for lvl up our skills in front and back
personally I don\'t read about yet but I think in reading about and learn at least 80%
"""

index = 0
for i in [1,'string',3]:
    print(index, i)
    index += 1
print('\n')

index = 0
variable = [1, 'pera', 5]
while index < len(variable):
    print('line 89', variable[index])
    index += 1

if len(variable) < index:
    print('minor')
elif len(variable) == index:
    print('equal')
else:
    print('major')

print()

my_dict = {
    'Franco': 19,
    'Juan': 20,
    'alumns':[
        {'name': 'franco', 'age': '19'},
        {'name': 'juan', 'age': '0'}
    ]
}

alumns = {'': 0 * (len(my_dict) - 1)} 
index = 1
list_names = []
list_ages = []
for key_name in my_dict:
    if len(my_dict) != index:
        list_names.append(key_name.title()) 
        list_ages.append(f'{my_dict[key_name]} years old')
        index += 1

print('line 120', list_names)
print('line 121', list_ages)
print('line 122', my_dict)

index = 0
alumns = my_dict['alumns']


while index < len(list_names):
    if alumns[index]['name'] != list_names[index]:
        alumns[index]['name'] = list_names[index]
    if alumns[index]['age'] != list_ages[index]:
        alumns[index]['age'] = list_ages[index]
    #the conditions there are for reduce the replacements
    index +=1


dict_with_years = []

def fill_dict(dict: list, data: dict, *args) -> dict:
    index = 0
    while index < len(list_names):
        inner_index = 0
        for arg in args:
            if inner_index == 0:
                dict.append({}) #avoiding index error without try catch
                dict[index] = {f'{arg}': data[index][f'{arg}']}
            else:
                dict[index] = {**dict[index]}, {f'{arg}': data[index][f'{arg}']}
            inner_index += 1
        index += 1

    return dict

dict_with_years = fill_dict(dict_with_years, alumns, 'name', 'age')

print('line 156', dict_with_years)
 
index = 0
for age in list_ages:
    alumns[index]['age'] = age.split(' ')[0]
    index += 1

dict_within_years = []

dict_within_years = fill_dict(dict_within_years, alumns, 'name', 'age')
print('line 166', dict_within_years)

#! Switch and do-while statements doesn't exist here
#* Ive got lazy but; normally i create a show function(line, color, message) to avoid repeat at myself in the print
#? To run in the terminal, press cntrl + j and write the script python about_python.py only if you have python installed previously