# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        sort(left)
        sort(right)

        i_l = i_r = j = 0
        len_l = len(left)
        len_r = len(right)

        while i_l < len_l and i_r < len_r:
            if left[i_l] < right[i_r]:
                array[j] = left[i_l]
                i_l += 1
            else:
                array[j] = right[i_r]
                i_r += 1
            j += 1

        while i_l < len_l:
            array[j] = left[i_l]
            j += 1
            i_l += 1

        while i_r < len_r:
            array[j] = right[i_r]
            j += 1
            i_r += 1


size = 10
a = [random.randint(0, 49) for _ in range(size)]
print('Исходный массив: ', a)
sort(a)
print('Отсортированный массив: ', a)
