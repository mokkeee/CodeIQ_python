# -*- coding: utf-8 -*-


def print_line(_size, _v_position):
    v_positions = {_v_position, int(_size - _v_position - 1)}
    for pos in range(0, _size):
        if pos in v_positions:
            print('v', end='')
        else:
            print('.', end='')
    print()


def print_last_line(_size):
    for pos in range(0, _size):
        if pos == int(_size / 2):
            print('v', end='')
        else:
            print('.', end='')
    print()


def print_vmark(_size):
    for v_pos in range(0, int(_size / 2)):
        print_line(_size, v_pos)
        print_line(_size, v_pos)
    print_last_line(_size)


def is_even_number(_num):
    return _num % 2 == 0


'''
1行目と2行目は左から1番目と右から1番目を「v」にします。
3行目以降は2行ごとに左右とも1列内側を「v」にします。
それ以外を半角ドット「.」にします。

・高さが奇数の場合は「進捗ヴェリーグッドマーク」を出力する
・高さが偶数の場合は「invalid」を出力する
'''
try:
    while True:
        size = int(input())
        if is_even_number(size):
            print('invalid')
            continue
        print_vmark(size)
except EOFError:
    pass
