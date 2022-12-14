from advent_of_code.utils import get_input

lines = get_input("test_input.txt")
lines = get_input("input.txt")


tuples = [tuple(elem.split(',')) for elem in lines]
tuple_tuples = [(tuple(a.split('-')),tuple(b.split('-'))) for a, b in tuples]
print(tuples)
print(tuple_tuples)

count = 0

for (a, b), (c, d) in tuple_tuples:
    a, b, c, d = int(a), int(b), int(c), int(d)

    left_overlapped = True
    right_overlapped = True
    if a < c:
        left_overlapped = False
        if b < c:
            right_overlapped = False
        elif d > b:
            right_overlapped = False
    elif c < a:
        right_overlapped = False
        if d < a:
            left_overlapped = False
        elif b > d:
            left_overlapped = False
    else:  # a==c
        if b < d:
            right_overlapped = False
        elif d < b:
            left_overlapped = False

    if left_overlapped or right_overlapped:
        count += 1

print("PART ONE")
print(count)

count = 0

for (a, b), (c, d) in tuple_tuples:
    a, b, c, d = int(a), int(b), int(c), int(d)

    if not (b < c or d < a):
        count += 1

print("PART TWO")
print(count)
