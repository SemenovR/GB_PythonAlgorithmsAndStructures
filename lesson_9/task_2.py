# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque
import operator


class Node:
    def __init__(self, left=None, right=None, value=None, count=0):
        self.left = left
        self.right = right
        self.value = value
        self.count = count


def encode_huffman(s):
    codes = {}  # Таблица кодов

    # Печать дерева
    def print_tree(n, level=0):
        tab = '\t' * level if level > 0 else ''
        print(f'{tab}Node(value={n.value}, count={n.count})')
        if n.left:
            print_tree(n.left, level=level + 1)
        if n.right:
            print_tree(n.right, level=level + 1)

    # Формирование таблицы кодов из дерева
    def get_codes(n, v=''):
        if n.left is None and n.right is None:
            codes[n.value] = v
        else:
            if n.left is not None:
                get_codes(n.left, v+'0')
            if n.right is not None:
                get_codes(n.right, v+'1')

    assert len(s) > 0, 'Строка не должна быть пустой'
    c = Counter(s)
    d = deque(map(lambda x: Node(value=x[0], count=x[1]), c.most_common()))

    while True:
        node_left = d.popleft()
        sum_count = node_left.count
        if d:
            node_right = d.popleft()
            sum_count += node_right.count
        else:
            node_right = None
        node = Node(left=node_left, right=node_right, count=sum_count)
        if d:
            d.append(node)
            d = deque(sorted(d, key=operator.attrgetter('count')))
        else:
            break

    # print_tree(node)
    get_codes(node)
    return " ".join(codes[si] for si in s)


print('Закодированная строка:', encode_huffman('beep boop beer!'))

