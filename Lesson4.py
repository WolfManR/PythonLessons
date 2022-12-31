import random

# 1     Напишите функцию (F): на вход список имен и целое число N;
#       на выходе список длины N случайных имен из первого списка (могут повторяться,
#       можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);


def length_of_some_names(names, number):
    list_of_length = []
    for i in range(number + 1):
        list_of_length.append(len(names[random.randint(0, len(names) - 1)]))
    return list_of_length


print(length_of_some_names(['yas', 'kate', 'loseta'], 10))

# 2     Напишите функцию вывода самого частого имени из списка на выходе функции F;


def very_known_name(names):
    temp = {}
    for name in names:
        temp[name] = 1 if name not in temp.keys() else temp[name] + 1
    return sorted(temp.items(), key=lambda pair: pair[1], reverse=True)[0][0]


print(very_known_name(['Yas', 'Kate', 'Kate', 'Loseta']))

# 3     Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.


def very_not_liked_char_in_names(names):
    temp = {}
    for name in names:
        char = name[0]
        temp[char] = 1 if char not in temp.keys() else temp[char] + 1
    return sorted(temp.items(), key=lambda pair: pair[1])[0][0]


print(very_not_liked_char_in_names(['Yas', 'Kate', 'Kate', 'Loseta']))