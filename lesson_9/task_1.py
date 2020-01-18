# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

import hashlib


def count_substring(s):
    length = len(s)
    assert length > 0, 'Строка не должна быть пустой'
    s = s.lower()
    unique_set = set()

    for i in range(length):
        for j in range(i, length + 1):
            ss = s[i:j]
            if not ss.isspace() and ss != '' and ss != s:    # Исключаем пустую строку и строку целиком
                unique_set.add(hashlib.sha1(ss.encode('utf-8')).hexdigest())

    return len(unique_set)


print('Количество различных подстрок:', count_substring(input('Введите строку: ')))
