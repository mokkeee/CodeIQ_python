#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_1_from_bin(num):
    return format(num, 'b').count('1')


FOR_BCD = {}
for num in range(0, 10):
    count = count_1_from_bin(num)
    FOR_BCD[str(num)] = count


def count_1_from_bcd(num):
    count = 0
    for digit in str(num):
        count += FOR_BCD[digit]
    return count


def count_ones_match(digits_number):
    output_count = 0
    start_num = 1 * 10**(digits_number-1)
    end_num = start_num * 10
    for num in range(start_num, end_num):
        if count_1_from_bin(num) == count_1_from_bcd(num):
            output_count += 1
    return output_count


try:
    while True:
        digits_number = int(input())
        output = count_ones_match(digits_number)
        print(output)
except EOFError:
    pass
