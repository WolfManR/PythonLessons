import random

from Lesson5 import division_master

get_random = lambda: random.randint(1, 1001)

# 1. Проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
number = get_random()
isSimple = division_master.is_simple(number)
print(f'{number} is{("" if isSimple else " not")} simple')

# 2. Выводит список всех делителей числа;
number = get_random()
dividers = division_master.dividers(number)
print(f'Dividers of {number} is: {dividers}')

# 3. Выводит самый большой простой делитель числа.
number = get_random()
biggestDivider = division_master.biggest_divider(number)
print(f'biggest divider of {number} is: {biggestDivider}')
