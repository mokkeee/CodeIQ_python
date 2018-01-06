#!/usr/bin/env python
# -*- coding: utf-8 -*-

GATES = {
    'a': ('7', 'D'),
    'b': ('E', 'F'),
    'c': ('G', 'M'),
    'd': ('A', 'B')
}

ROUTES = [
    ('0', '6'),
    ('1', '2'),
    ('2', '3'),
    ('2', '8'),
    ('3', '4'),
    ('4', '5'),
    ('4', 'A'),
    ('6', '7'),
    ('7', '8'),
    ('9', 'A'),
    ('9', 'F'),
    ('A', 'G'),
    ('B', 'H'),
    ('C', 'D'),
    ('D', 'J'),
    ('E', 'K'),
    ('H', 'N'),
    ('I', 'J'),
    ('I', 'O'),
    ('J', 'P'),
    ('J', 'K'),
    ('K', 'L'),
    ('M', 'N'),
    ('M', 'S'),
    ('N', 'T'),
    ('O', 'U'),
    ('Q', 'R'),
    ('Q', 'W'),
    ('R', 'S'),
    ('T', 'Z'),
    ('U', 'V'),
    ('V', 'W'),
    ('X', 'Y'),
    ('Y', 'Z')
]

POINT_NAMES = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')

INFINITY = float('inf')


class Point:
    def __init__(self, name):
        self._name = name
        self._cost = INFINITY
        self._done = False

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    def is_done(self)->bool:
        return self._done

    def can_done(self)->bool:
        if self.is_done():
            return False
        if self.cost == INFINITY:
            return False
        return True

    def done(self):
        self._done = True

    def __str__(self):
        return ", ".join([self._name, str(self.cost), str(self._done)])


def next_point(_current, _routes):
    for route in _routes:
        if _current in route:
            yield route[1] if route[0] == _current else route[0]


def get_min_step_count(_start, _goal, _routes):
    points = {}
    for name in POINT_NAMES:
        points[name] = Point(name)
    points[_start].cost = 0

    while True:
        nodes = list(filter(lambda n: n.can_done(), points.values()))
        if len(nodes) == 0:
            break

        done_node = min(nodes, key=lambda n: n.cost)
        done_node.done()
        next_cost = done_node.cost + 1

        for _next in next_point(done_node.name, _routes):
            if points[_next].cost > next_cost:
                points[_next].cost = next_cost

    for v in sorted(points.values(), key=lambda n: n.name):
        print(v)
    return points[_goal].cost


try:
    while True:
        gate, start, goal = list(input())
        routes = ROUTES.copy()
        routes.append(GATES[gate])
        min_step_count = get_min_step_count(start, goal, routes)
        print(min_step_count)
except EOFError:
    pass

