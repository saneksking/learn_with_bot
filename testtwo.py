"""Перемннные"""
x = 10
y = 15
z = x + y
print(z)
print('-' * 80)
"""Типы данных"""
num = 15
string = "Hello, world!"
float_num = 1.55
nums = [1, 2, 3, 4, 5]
key_value = {'Hello': 'World', 'Hey': 'Guys'}
special = {1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 7, 8, 9, 0, 0}
names = ('Alex', 'Steve', 'Max')
print(type(num), type(string), type(float_num), type(nums), type(key_value), type(special), type(names), special)
"""Условия"""
x = 15
if x == 15:
    print('x равно 15')
else:
    print('x не равно 15')

y = 26
if y == 25:
    print('y равно 25')
else:
    print('y не равно 25')

if x == 15:
    if x + 5 == 20:
        print('x равно 20')
else:
    print('x не равно 15')
