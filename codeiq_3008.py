#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'

import re


MYSTERY_NUMBER = '[0-9.]+'
OS_NAME = '[A-Za-z0-9 ]+'
GENERAL_PATTERN = '[A-Za-z0-9.]+'


def is_match_in_pattern(pattern, user_agent):
    return pattern.fullmatch(user_agent)


def is_match_in_patterns(patterns, user_agent):
    for pattern in patterns:
        if pattern.fullmatch(user_agent) is not None:
            return True
    else:
        return False


def is_Mamella_Firedog(user_agent):
    Mamella_Firedog_Pattern = re.compile('Mamella/5.0 \(%s\) Lizard/%s Firedog/%s'
                                         % (OS_NAME, GENERAL_PATTERN, GENERAL_PATTERN))
    return is_match_in_pattern(Mamella_Firedog_Pattern, user_agent)


def is_Orange_Voyage(user_agent):
    Orange_Voyage_Pattern = re.compile('Mamella/5.0 \(%s\) OrangeKit/%s \(like Lizard\) Version/%s Voyage/%s'
                                       % (OS_NAME, GENERAL_PATTERN, GENERAL_PATTERN, MYSTERY_NUMBER))
    return is_match_in_pattern(Orange_Voyage_Pattern, user_agent)


def is_AnachroSoft_Internet_Traveller(user_agent):
    AnachroSoft_Internet_Traveller_Patterns = [
        re.compile('Mamella/4.0 \(compatible; ASIT %s; %s\)' % (GENERAL_PATTERN, OS_NAME)),
        re.compile('Mamella/5.0 \(compatible; ASIT %s; %s\)' % (MYSTERY_NUMBER, OS_NAME)),
        re.compile('Mamella/5.0 \(%s; Quadent/7.0; .KNOT SLR; rv:4.0\) like Lizard' % OS_NAME),
        re.compile(
            'Mamella/5.0 \(%s; Quadent/7.0\) OrangeKit/12.0 Firedog/3.0 \(like Lizard\) Voyage/4.0 ASIT/12.0' % OS_NAME)
    ]
    return is_match_in_patterns(AnachroSoft_Internet_Traveller_Patterns, user_agent)


def is_Kabuki_Browser(user_agent):
    Kabuki_Browser_Patterns = [
        re.compile('Mamella/4.0 \(%s\) Kabuki %s' % (OS_NAME, MYSTERY_NUMBER)),
        re.compile('Mamella/4.0 \(compatible; ASIT 6.0; ASIT 5.5; %s\) Kabuki %s' % (OS_NAME, MYSTERY_NUMBER)),
        re.compile('Kabuki/%s \(%s\) Lento/%s' % (MYSTERY_NUMBER, OS_NAME, GENERAL_PATTERN)),
        re.compile(
            'Mamella/5.0 \(%s\) OrangeKit/%s \(like Lizard\) Monochrome/%s Voyage/%s KBK/%s'
            % (OS_NAME, MYSTERY_NUMBER, MYSTERY_NUMBER, MYSTERY_NUMBER, GENERAL_PATTERN))
    ]
    return is_match_in_patterns(Kabuki_Browser_Patterns, user_agent)


def is_Gluegle_Monochrome(user_agent):
    Gluegle_Monochrome_Patterns = [
        re.compile('Mamella/5.0 \(%s\) OrangeKit/%s \(like Lizard\) Monochrome/%s Voyage/%s' % (
            OS_NAME, GENERAL_PATTERN, GENERAL_PATTERN, MYSTERY_NUMBER)),
        re.compile('Mamella/5.0 \(%s\) OrangeKit/%s \(like Lizard\) Monochrome/%s Voyage/%s' % (
            OS_NAME, MYSTERY_NUMBER, GENERAL_PATTERN, MYSTERY_NUMBER))
    ]
    return is_match_in_patterns(Gluegle_Monochrome_Patterns, user_agent)


def judge_browser(param):
    targets = [
        (is_Mamella_Firedog, 'MFD'),
        (is_Orange_Voyage, 'VYG'),
        (is_AnachroSoft_Internet_Traveller, 'ASIT'),
        (is_Kabuki_Browser, 'KBK'),
        (is_Gluegle_Monochrome, 'GMC')
    ]
    for target in targets:
        if target[0](param):
            return target[1]


if __name__ == '__main__':
    try:
        while True:
            print(judge_browser(input()))
    except EOFError:
        pass


def test_judge_browser():
    assert judge_browser('Mamella/5.0 (Fen32) Lizard/20050919 Firedog/1.0.0') == 'MFD'
    assert judge_browser('Mamella/4.0 (compatible; ASIT 5.5; Fenetre Testament)') == 'ASIT'
