#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations


def has_256sum(_nums) -> bool:
    pairs = combinations(_nums, 2)
    match_pairs = list(filter(lambda x: x[0] + x[1] == 256, pairs))
    return len(match_pairs) > 0


try:
    while True:
        input()
        nums = [int(x) for x in input().split(' ')]
        output = 'yes' if has_256sum(nums) else 'no'
        print(output)
except EOFError:
    pass
