# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(0, 1000) for _ in range(10)]
print(f'Исходный массив: {a}')

min_i = max_i = 0

for i, v in enumerate(a):
    if v < a[min_i]:
        min_i = i
    if v > a[max_i]:
        max_i = i

a[min_i], a[max_i] = a[max_i], a[min_i]
print(f'Результирующий массив: {a}')