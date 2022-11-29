# Задание 3 - Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random
print()
number=int(input('Введите целое число более 1: '))
rand_list=[]
for i in range(0,number):
    rand_list.append(random.randint(-10,0))
print('Исходный массив')
print(rand_list)
for j,item in enumerate(rand_list):
    if item <0:
        rand_list.insert(j+1, 0)
print('Конечный массив')
print(rand_list)