from advent_of_code.utils import get_input

#lines = get_input("test_input.txt")
lines = get_input("input.txt")

head = (0,0)
tail = (0,0)

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

def perform_move(h, t, direction, steps):
    for _ in range(steps):
        h = add_step(h, get_step_tuple(direction))
        if apart(h, t):
            h, t = same_lining(h, t, direction)
            t = add_step(t, get_step_tuple(direction))
            global pos
            pos.add(t)
    return h, t

def print_ht(h,t):
    x_max = max([h[0], t[0], 0])
    x_min = min([h[0], t[0], 0])
    y_max = max([h[1], t[1], 0])
    y_min = min([h[1], t[1], 0])

    result = ''
    for y in range(y_max+1, y_min-2, -1):
        for x in range(x_min-1, x_max+2):
            if (x, y) == h:
                result += 'H'
            elif (x,y) == t:
                result += 'T'
            elif (x,y) == (0,0):
                result += 's'
            else:
                result += '.'
        result += '\n'

    print(result)

print_ht(head, tail)
for line in lines:
    direction, steps = line.split(' ')
    head, tail = perform_move(head, tail, direction, int(steps))
    print_ht(head, tail)

print(f"Tail visited {len(pos)} fields")
