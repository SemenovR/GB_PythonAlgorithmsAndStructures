# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается
# в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование
# встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque

LIST_NUMBERS = list('0123456789ABCDEF')
DICT_NUMBERS = {n: i for i, n in enumerate(LIST_NUMBERS)}
ZERO = '0'
NUM_SYSTEM = 16


def hex_sum(vn1, vn2):
    dn1 = deque(vn1)
    dn2 = deque(vn2)
    result = deque()
    reminder = 0

    while dn1 or dn2:
        s = DICT_NUMBERS[dn1.pop() if dn1 else ZERO] + DICT_NUMBERS[dn2.pop() if dn2 else ZERO] + reminder
        reminder = s // NUM_SYSTEM
        result.appendleft(LIST_NUMBERS[s % NUM_SYSTEM])

    if reminder:
        result.appendleft(LIST_NUMBERS[reminder])

    return result


def hex_multi(vn1, vn2):
    temp = deque()
    result = deque()
    multi = 0

    for i2 in reversed(vn2):
        reminder = 0
        for i in range(multi):
            temp.appendleft('0')
        for i1 in reversed(vn1):
            m = DICT_NUMBERS[i1] * DICT_NUMBERS[i2] + reminder
            reminder = m // NUM_SYSTEM
            temp.appendleft(LIST_NUMBERS[m % NUM_SYSTEM])
        if reminder:
            temp.appendleft(LIST_NUMBERS[reminder])
        result = hex_sum(result, temp)
        temp.clear()
        multi += 1

    return result


if __name__ == '__main__':
    n1 = list(input("Введите число 1: ").upper())
    n2 = list(input("Введите число 2: ").upper())

    if not all((c in LIST_NUMBERS) for c in n1):
        print("Число 1 содержит неверные символы!")
        exit()
    if not all((c in LIST_NUMBERS) for c in n2):
        print("Число 2 содержит неверные символы!")
        exit()

    print(f'Сумма чисел: {hex_sum(n1, n2)}')
    print(f'Произведение чисел: {hex_multi(n1, n2)}')
