# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import cProfile


def sieve_eratosthenes(k):
    n = 10000000
    sieve = [i for i in range(n)]
    sieve[1] = 0
    length = 0
    res = 0

    for i in range(2, n):
        if sieve[i] != 0:
            if length == k:
                res = sieve[i]
                break
            length += 1

            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i

    return res


def classic_method(k):
    simple = [2, ]
    i = 0
    value = 2
    while i < k:
        value += 1
        for s in simple:
            if value % s == 0:
                break
        else:
            simple.append(value)
            i += 1

    return value


def test(i):
    print(f'Решето Эратосфена {sieve_eratosthenes(i)}')
    print(f'Классический способ: {classic_method(i)}')


def main(i):
    sieve_eratosthenes(i)
    classic_method(i)


#test(1000)
#test(5000)
#test(10000)
#test(50000)


cProfile.run('main(1000)')
cProfile.run('main(5000)')
cProfile.run('main(10000)')
cProfile.run('main(50000)')

# Результаты замеров.
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# i = 1000
#         1    3.996    3.996    4.328    4.328 task_2.py:13(sieve_eratosthenes)
#         1    0.036    0.036    0.036    0.036 task_2.py:35(classic_method)
# i = 5000
#         1    4.373    4.373    4.702    4.702 task_2.py:13(sieve_eratosthenes)
#         1    0.826    0.826    0.827    0.827 task_2.py:35(classic_method)
# i = 10000
#         1    4.493    4.493    4.823    4.823 task_2.py:13(sieve_eratosthenes)
#         1    3.486    3.486    3.487    3.487 task_2.py:35(classic_method)
# i = 50000
#         1    4.782    4.782    5.111    5.111 task_2.py:13(sieve_eratosthenes)
#         1   81.267   81.267   81.272   81.272 task_2.py:35(classic_method)
#
# Из результатов видно что классический алгоритм быстрее при неболльших значениях i.
# Но с увеличением i скорость начинает падать и в лидеры выходит Решето Эратосфена.
# Однако медленная скорость Решета Эратосфена при небольших i связана с тем, что число n (длина решета) в функции
# задано постоянно большим (10000000), чтобы можно было вычислить большие простые числа.
# Если при каждом запуске подгонять это число более близко к искомому результату, то Решето Эратосфена
# будет быстрее при всех вариантах. Результат с подогнанным n ниже.

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# i = 1000, n = 10000
#         1    0.004    0.004    0.004    0.004 task_2.py:13(sieve_eratosthenes)
#         1    0.034    0.034    0.034    0.034 task_2.py:35(classic_method)
# i = 5000, n = 100000
#         1    0.037    0.037    0.041    0.041 task_2.py:13(sieve_eratosthenes)
#         1    0.812    0.812    0.812    0.812 task_2.py:35(classic_method)
# i = 10000, n = 1000000
#         1    0.368    0.368    0.402    0.402 task_2.py:13(sieve_eratosthenes)
#         1    3.245    3.245    3.246    3.246 task_2.py:35(classic_method)
# i = 50000, n = 10000000
#         1    4.654    4.654    4.999    4.999 task_2.py:13(sieve_eratosthenes)
#         1   78.974   78.974   78.978   78.978 task_2.py:35(classic_method)
#
# Вывод: Решето Эратосфена быстрее классического алгоритма, но требует указания длины решета.
