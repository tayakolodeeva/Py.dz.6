# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#numbers = list(map(int, input('Введите числа (разделяя пробелом):\n').split()))
#l = len(numbers)//2 + 1 if len(numbers) % 2 != 0 else len(numbers)//2
#res = [numbers[i]*numbers[len(numbers)-i-1] for i in range(l)]
#print(f'Произведение пар чисел списка {numbers}, равно: {res}')

import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print(f'Произведение пар чисел списка {list_a}, равно:',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))