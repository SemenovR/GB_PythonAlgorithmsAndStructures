# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a = [random.randint(0, 1000) for _ in range(10)]
s = min_i = max_i = 0

for i, v in enumerate(a):
    if v < a[min_i]:
        min_i = i
    if v > a[max_i]:
        max_i = i

if min_i > max_i:
    min_i, max_i = max_i, min_i

for i in range(min_i + 1, max_i):
    s += a[i]

print(f'a = {a}')
print(f'min_i, max_i = {min_i, max_i}')
print(f'Сумма = {s}')