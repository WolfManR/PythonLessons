
# 1     Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
print('Task 1: 5 string with 0 and it index')
for i in range(5):
    print((i + 1).__str__() + " 0")

# 2     Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
print('\nTask 2: how many times user input number 5')
input5TimesCounter = 0
for i in range(10):
    userInput = input((i + 1).__str__() + ': input a number ')
    if userInput.isdigit() and float(userInput) == 5:
        input5TimesCounter += 1
print('you input 5 times: ' + input5TimesCounter.__str__())

# 3     Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
print('\nTask 3: sum of numbers from 1 to 100')
sumOfNumbers = 0
for i in range(1, 101):
    sumOfNumbers += i
print('sum of numbers equals ' + sumOfNumbers.__str__())

# 4     Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
print('\nTask 4: multiply of numbers from 1 to 10')
multiplyOfNumbers = 1
for i in range(1, 10, 1):
    multiplyOfNumbers *= i
print('multiply of numbers equals ' + multiplyOfNumbers.__str__())

# 5     Вывести цифры числа на каждой строчке.
print('\nTask 5: print numbers of number')
inputNumber = ''
while not inputNumber.isdigit():
    inputNumber = input('your number please ')
for i in range(len(inputNumber)):
    print(inputNumber[i])

