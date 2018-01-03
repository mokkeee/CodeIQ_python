#!/usr/bin/env python
# -*- coding: utf-8 -*-


NAMES_1to9 = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'}

NAMES_10to19 = {
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

NAMES_20to90 = {
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety'}

THOUSAND = 10 ** 3
MILLION = 10 ** 6
BILLION = 10 ** 9

MAX_32BIT = 0x7fffffff


def english_name_words(_number):
    if _number < 0:
        yield 'Negative'
        _number *= -1

    if _number == 0:
        yield 'Zero'
    elif _number < 10:
        yield NAMES_1to9[_number]
    elif _number < 20:
        yield NAMES_10to19[_number]
    elif _number < 100:
        yield NAMES_20to90[int(_number / 10) * 10]
        remain_under10 = _number % 10
        if remain_under10 > 0:
            yield NAMES_1to9[remain_under10]
    elif _number < THOUSAND:
        yield NAMES_1to9[int(_number / 100)]
        yield 'Hundred'
        remain_under100 = _number % 100
        if remain_under100 > 0:
            yield from english_name_words(remain_under100)
    elif _number < MILLION:
        number_over1000 = int(_number / THOUSAND)
        number_under1000 = _number % THOUSAND
        yield from english_name_words(number_over1000)
        yield 'Thousand'
        if number_under1000 > 0:
            yield from english_name_words(number_under1000)
    elif _number < BILLION:
        number_over_million = int(_number / MILLION)
        number_under_million = _number % MILLION
        yield from english_name_words(number_over_million)
        yield 'Million'
        if number_under_million > 0:
            yield from english_name_words(number_under_million)
    elif _number <= MAX_32BIT:
        number_over_billion = int(_number / BILLION)
        number_under_billion = _number % BILLION
        yield from english_name_words(number_over_billion)
        yield 'Billion'
        if number_under_billion > 0:
            yield from english_name_words(number_under_billion)
    else:
        raise NotImplementedError()


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

