# -*- coding: utf-8 -*-


def before_center(_size, _current):
    for pos in range(0, _size):
        if pos == 0:
            print('m', end="")
        elif pos == (_size - 1):
            print('m', end="")
        elif pos == _current:
            print('m', end="")
        elif pos == (_size - _current - 1):
            print('m', end="")
        else:
            print('.', end="")
    print('')


def after_center(_size):
    print('m', end="")
    print('.' * (_size - 2), end="")
    print('m')


def is_even_number(_num):
    return _num % 2 == 0


def center(_size):
    return int(_size / 2)


'''
すべての行の左右の端は「m」です。
1行目から真ん中の行までは
R行目の場合に、左からR列目と右からR列目を「m」にします。
それ以外を半角ドット「.」にします。
'''
try:
    while True:
        size = int(input())
        if is_even_number(size):
            print('invalid')
            continue

        for row in range(0, center(size)):
            before_center(size, row)
        for row in range(center(size), size):
            after_center(size)
except EOFError:
    pass
