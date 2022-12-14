import enum
import string
from typing import List

from advent_of_code.utils import get_input

lines = get_input("test_input.txt")
#lines = get_input("input.txt")

snail = [(0,0) for _ in range(10)]

def get_step_tuple(direction):
    if direction == 'R':
        return (1, 0)
    if direction == 'L':
        return (-1, 0)
    if direction == 'U':
        return (0, 1)
    if direction == 'D':
        return (0, -1)

def apart(h, t):
    #
    #   111
    #   1T1
    #   111
    #

    if abs(h[0]-t[0]) < 2 and abs(h[1]-t[1]) < 2:
        return False
    return True

def same_lining(h, t, direction):
    if direction in ['R', 'L']:
        # horizontal
        # check vertical
        if h[1] != t[1]:
            return h, (t[0], h[1])
    elif direction in ['U', 'D']:
        # vertical
        # check horizontal
        if h[0] != t[0]:
            return h, (h[0], t[1])
    else:
        raise Exception(f"unpredicted move direction '{direction}'")
    return h, t

def add_step(knot, step):
    return (knot[0]+step[0], knot[1]+step[1])

pos = set()

def perform_move(h, t, direction, steps, tail=False):
    for _ in range(steps):
        h = add_step(h, get_step_tuple(direction))
        if apart(h, t):
            h, t = same_lining(h, t, direction)
            t = add_step(t, get_step_tuple(direction))
            if tail:
                global pos
                pos.add(t)
    return h, t

def print_ht(h,s):
    x_max = max([h[0], 0] + [knot[0] for knot in s])
    x_min = min([h[0], 0] + [knot[0] for knot in s])
    y_max = max([h[1], 0] + [knot[1] for knot in s])
    y_min = min([h[1], 0] + [knot[1] for knot in s])

    result = ''
    for y in range(y_max+1, y_min-2, -1):
        for x in range(x_min-1, x_max+2):

            if (x, y) == h:
                result += 'H'
            elif any([(x,y) == knot for knot in s]):
                result += str([(x, y) == knot for knot in s].index(True)+1)
            elif (x,y) == (0,0):
                result += 's'
            else:
                result += '.'
        result += '\n'

    print(result)

print_ht(snail[0], snail[1:])
for line in lines:
    direction, steps = line.split(' ')

    for _ in range(int(steps)):
        for i in range(1, len(snail)):
            tail = False
            if i == len(snail)-1:
                tail = True
            if i == 1:
                snail[i-1] = add_step(snail[i-1], get_step_tuple(direction))
            if apart(snail[i-1], snail[i]):
                snail[i-1], snail[i] = same_lining(snail[i-1], snail[i], direction)
                snail[i] = add_step(snail[i], get_step_tuple(direction))
                if tail:
                    pos.add(snail[i])

    print_ht(snail[0], snail[1:])

print(f"Tail visited {len(pos)} fields")

