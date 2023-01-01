# 1. Проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def is_simple(number):
    count = 0
    for i in range(1, number):
        count = count if number % i > 0 else count + 1
        if count > 2:
            return False
    return True if count == 2 else False


# 2. Выводит список всех делителей числа;
def dividers(number):
    numbers = []
    for i in range(1, number):
        if number % i > 0:
            numbers.append(i)

    return numbers


# 3. Выводит самый большой простой делитель числа.

def biggest_divider(number):
    if is_simple(number):
        return number

    max_simple_number = 0
    for i in range(1, number):
        if not number % i > 0:
            continue
        if is_simple(i):
            max_simple_number = i
    return max_simple_number
