"""
def prime_number(n, i=2):
    if n == 1 or n == 2:
        return True
    elif n % i == 0:
        return False
    elif i*i>n:
        return True    
    return prime_number(n, i+1)

print(prime_number(101))
"""

'''
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f'{k}'


n = int(input())
print(f(n))
'''

'''
def sum(a, b):
  if b == 0:
    return a;
  return f(a, b - 1) + 1
'''

#Задача No41. Решение в группах
#Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у
# которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество 
# элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод: Ввод:
# 55
# 1 2 3 4 5 15151
# Вывод: Вывод:
# 02

'''
number = int(input('Введите число: '))
lst = []

for _ in range(number):
    lst.append(int(input('Введите числа: ')))

count = 0

for i in range(1, len(lst) - 1):
    if lst[i + 1] < lst[i] > lst[i - 1]:
        count += 1

print(*lst)
print(count)
'''

'''
n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))
'''
   
'''
    n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))
'''

# Д/з
# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

'''
array = []
A = int(input('Введите первый элемент массива: '))
d = int(input('Введите разность для формулы: '))
N = int(input('Введите количество элементов: '))
print('Последовательность: ')
for i in range(N):
    array.append(A + d) 
    print(A)
    A= A + d
'''

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)

'''
import random
N = int(input('Введите количество элементов: '))
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))

list = []
for i in range(N):
    list.append(random.randint(0, 101))
print(list)

ind_list = []
for i in range(len(list)):
    if list[i] >= min and list[i] <= max:
        ind_list.append(i)

print(ind_list)
'''
