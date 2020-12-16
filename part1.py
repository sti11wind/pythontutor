
import math


# Задача «Сумма трёх чисел»
a = int(input())
b = int(input())
с = int(input())
print(a + b + с)

#Ввод и вывод данных

b = int(input())
h = int(input())

print (1/2*b*h)

#Задача «Дележ яблок»


n = int(input('Колличество школьников '))
k = int(input('Колличество яблок '))
print(f'Ябло каждому {n // k} остаток в корзине {n % k}')



#Задача «Электронные часы»

n = int(input('Введите минуты '))
print(f'Прошло {n//60} часов и {n % 60} минут')


# Задача «Hello, Harry!»

name = str(input('Введите имя '))
print(f'Hello, {name}!')

# Задача «Следующее и предыдущее»



number = int(input('Введте число '))
print(f'The next number for the number {number} is {number + 1}.')

# Задача «Парты»

class1 = int(input('Введите колличество учеников 1ого класса '))
class2 = int(input(' Введите колличество учеников 2ого класса '))
class3 = int(input(' Введите колличество учеников 3ого класса '))
print(f'Всего нужно закупить  парт {math.ceil(class1 / 2) + math.ceil(class2  / 2) + math.ceil(class3 /2)}')



#Задача «Шнурки»
a = int(input('Расстояние между рядами '))
b = int(input('Расстояние между дырочками в ряду '))
l = int(input('Количество дырочек в каждом ряду '))
n = int(input('длина свободного конца шнурка '))
print(f'{(2 * l + (2 * n - 1) * a + 2 * (n - 1) * b)}')
