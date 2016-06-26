#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'

import pytest

import re
from functools import reduce

erase_pattern = re.compile('[0-6,8-9]+')

def seven_count_in_number(num):
    return len(erase_pattern.sub('', str(num)))


def seven_count(max_num):
    count = reduce(
        lambda x, y: x+y,
        map(seven_count_in_number,
            range(1, max_num+1)))
    #numbers = re.sub('[0-6,8-9]+', '',
    #    ''.join(
    #        filter(
    #            lambda s: '7' in s,
    #            map(str, range(1, max_num+1)))))
    # numbers = re.sub('[0-6,8-9]+', '',
        # ''.join(map(str, range(1, max_num+1))))
    return count


if __name__ == '__main__':
    try:
        while True:
            input_num = int(input())
            print(seven_count(input_num))
    except EOFError:
        pass


def test_count():
    assert seven_count_in_number('177') == 2
    assert seven_count(10) == 1     # 7
    assert seven_count(20) == 2     # 7 17
    assert seven_count(99) == 20
