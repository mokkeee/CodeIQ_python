#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'


def primes(max_number):
    if max_number <= 2:
        raise StopIteration
    yield 2
    is_prime = [1] * max_number
    square_root_of_max = max_number ** 0.5
    for number in range(3, max_number, 2):
        if is_prime[number] is 0:
            continue
        yield number
        if number <= square_root_of_max:
            for multiple in range(number * 2, max_number, number):
                is_prime[multiple] = 0


def count_prime_distributions(max_num, num_range):
    distribution_count_dict = {}
    for prime in primes(max_num+1):
        key = int((prime-1) / num_range)
        distribution_count_dict[key] = distribution_count_dict.get(key, 0) + 1
    return distribution_count_dict


def print_prime_distributions(max_num, num_range):
    distribution_count_dict = count_prime_distributions(max_num, num_range)

    # print(distribution_count_dict)
    digits = len(str(max_num))
    num_format = '%0' + str(digits) + 'd'
    range_format = num_format + '-' + num_format + ':'
    for base, count in distribution_count_dict.items():
        num_min = 1 + base*num_range
        num_max = (base+1) * num_range
        print((range_format % (num_min, num_max)) + '*' * count)


if __name__ == '__main__':
    try:
        while True:
            (x, y) = input().split(" ")
            print_prime_distributions(int(x), int(y))
    except EOFError:
        pass


def test_prime_distributions():
    assert count_prime_distributions(30, 5) == {0: 3, 1: 1, 2: 2, 3: 2, 4: 1, 5: 1}

