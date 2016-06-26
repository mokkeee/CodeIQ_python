#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'

import pytest

from multiprocessing import Pool


def is_prime(target):
    if target == 1:
        return False
    if target == 2:
        return True
    for x in range(2, target):
        if target % x == 0:
            return False
    else:
        return True


def prime_count(param):
    prime_numbers = [x for x in range(1, param) if is_prime(x)]
    return len(prime_numbers)


def prime_count_multi(param):
    p = Pool(8)
    return len([x for x in p.map(is_prime, range(1, param)) if x])


def prime_count2(max_num):
    no_prime_numbers = set([])
    prime_count = 0
    for num in range(2, max_num):
        if num in no_prime_numbers:
            continue
        prime_count += 1
        no_prime_numbers.update(range(num*2, max_num, num))
    else:
        return prime_count


if __name__ == '__main__':
    try:
        while True:
            input_num = int(input())
            # print(prime_count_multi(input_num))
            # print(prime_count(input_num))
            print(prime_count2(input_num))
    except EOFError:
        pass


def assert_count(input_num, result):
    assert prime_count(input_num) == result
    assert prime_count_multi(input_num) == result
    assert prime_count2(input_num) == result


def test_count():
    assert_count(5, 2)  # 2, 3
    assert_count(10, 4) # 2, 3, 5, 7
    assert_count(11, 4) # 2, 3, 5, 7
    assert_count(12, 5) # 2, 3, 5, 7, 11
    assert_count(13, 5) # 2, 3, 5, 7, 11
    assert_count(14, 6) # 2, 3, 5, 7, 11, 13
    assert_count(20, 8) # 2, 3, 5, 7, 11, 13, 17, 19
    assert_count(25, 9) # 2, 3, 5, 7, 11, 13, 17, 19, 23
