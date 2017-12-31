#!/usr/bin/env python
# -*- coding: utf-8 -*-


names_1to9 = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'}

names_10to19 = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    19: 'Nineteen',
    18: 'Eighteen'}

names_20to90 = {
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety'}

words = [

    'Billion']


def english_name_words(_number):
    if _number < 0:
        yield 'Negative'
        _number *= -1

    if _number == 0:
        yield 'Zero'
    elif _number < 10:
        yield names_1to9[_number]
    elif _number < 20:
        yield names_10to19[_number]
    elif _number < 100:
        yield names_20to90[int(_number / 10) * 10]
        remain_under10 = _number % 10
        if remain_under10 > 0:
            yield names_1to9[remain_under10]
    elif _number < 1000:
        yield names_1to9[int(_number / 100)]
        yield 'Hundred'
        remain_under100 = _number % 100
        if remain_under100 > 0:
            for word in english_name_words(remain_under100):
                yield word
    elif _number < 1000 ** 2:
        number_1000 = int(_number / 1000)
        number_under1000 = _number % 1000
        for word in english_name_words(number_1000):
            yield word
        yield 'Thousand'
        if number_under1000 > 0:
            for word in english_name_words(number_under1000):
                yield word
    elif _number < 1000 ** 3:
        number_million = int(_number / (1000 ** 2))
        number_under_million = _number % (1000 ** 2)
        for word in english_name_words(number_million):
            yield word
        yield 'Million'
        if number_under_million > 0:
            for word in english_name_words(number_under_million):
                yield word
    else:
        number_billion = int(_number / (1000 ** 3))
        number_under_billion = _number % (1000 ** 3)
        for word in english_name_words(number_billion):
            yield word
        yield 'Billion'
        if number_under_billion > 0:
            for word in english_name_words(number_under_billion):
                yield word


def to_english_number(_number):
    value = list(english_name_words(_number))
    return ' '.join(value)


try:
    values_len = int(input())
    numbers = [int(input()) for i in range(0, values_len)]
    for number in numbers:
        print_name = to_english_number(number)
        print(print_name)
except EOFError:
    pass

