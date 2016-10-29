#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'

LOWER_VOWELS = 'aiueo'
UPPER_VOWELS = LOWER_VOWELS.upper()
VOWELS = LOWER_VOWELS + UPPER_VOWELS


def has_vowel(val):
    for vowel in VOWELS:
        if vowel in val:
            return True
    else:
        return False


def convert_string(val):
    if has_vowel(val):
        return val.upper()
    else:
        return val.lower()


if __name__ == '__main__':
    try:
        while True:
            print(convert_string(input()))
    except EOFError:
        pass


def test_convert():
    assert convert_string('YZjBo') == 'YZJBO'
    assert convert_string('tGlFy') == 'tglfy'
