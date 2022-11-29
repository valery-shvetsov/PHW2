# Задание 2 - Напишите программу, которая принимает на вход число N 
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

print()
number=int(input('Введите целое число более 1: '))
list_mult = [i for i in range(1, number+1)]
#print (list_mult)
for i in range(1, number):
    list_mult[i]=list_mult[i-1]*(i+1)
print (list_mult)
