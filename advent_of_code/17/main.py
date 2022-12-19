from advent_of_code.utils import get_input

line = get_input("test_input.txt")[0]
#line = get_input("input.txt")[0]


rock_line = 0b1111
rock_plus = 0b01000001110000010
# wir schreiben dir bits von links nach rechts
rock_r_l = 0b10000001000000111
rock_pillar = 0b1000000100000010000001
rock_block = 0b110000011

X_DIM = 7

INSERT_INDEX = 2
# INSERT_HEIGHT = heighest Rock plus 3

# gas, fall, gas fall

ROCK_ORDER = [
    rock_line, rock_plus, rock_r_l, rock_pillar, rock_block
]

rock_counter = 0

from itertools import cycle

rock_cycle = cycle(ROCK_ORDER)
push_cycle = cycle(line)

corridor = 0b1111111
height = 0

def print_corridor(c):
    c_str = bin(c)[2:]
    print("---Corridor---")
    lines = [c_str[i-X_DIM:i][::-1] for i in range(len(c_str), X_DIM-1, -X_DIM)]
    lines.append(c_str[0:len(c_str)%X_DIM][::-1])
    print("\n".join(lines[::-1]))
    print("")

print_corridor(corridor)

import math, time

start = time.time()

for rock in rock_cycle:
    rock_counter += 1
    if rock_counter == 2023:
        break
    # insert
    rock_corridor = rock << 2+3*X_DIM  # two '0' from the side + 3 empty lines
    rock_corridor = rock_corridor << math.ceil(corridor.bit_length() / X_DIM) * X_DIM
    #print_corridor(corridor | rock_corridor)
    for v in push_cycle:
        # push
        places_in_highest_row = rock_corridor.bit_length() % X_DIM
        if v == '<':
            # rock.bit_length() % X_DIM == ganz am Rand
            if not places_in_highest_row or places_in_highest_row > rock.bit_length() % X_DIM:
                # left == rechtsshift (wegen initialem linksshift für den 2er Abstand
                attempt_push = rock_corridor >> 1
                if attempt_push & corridor == 0:
                    rock_corridor = attempt_push
        elif v == '>':
            # == 0 -> volle row == am Rand
            if places_in_highest_row > 0:
                # right == linksshift
                attempt_push = rock_corridor << 1
                if attempt_push & corridor == 0:
                    rock_corridor = attempt_push
        else:
            raise Exception(f"Unknown Push direction {v}")

        #print_corridor(corridor | rock_corridor)
        # fall
        attempt_fall = rock_corridor >> X_DIM
        # check stop
        if attempt_fall & corridor == 0:
            rock_corridor = attempt_fall
        else:
            break

        #print_corridor(corridor | rock_corridor)

    corridor = corridor | rock_corridor
    #print_corridor(corridor)

    # shorten (string for now)
    if False:
        c_str = bin(corridor)[2:]
        lines = [c_str[i - X_DIM:i][::-1] for i in range(len(c_str), X_DIM - 1, -X_DIM)]
        #lines.append(c_str[0:len(c_str) % X_DIM][::-1])
        blocker = 0b0000000
        for j, l in enumerate(lines[:0:-1]):
            blocker |= int(l, 2)
            if blocker == 0b1111111:
                height_to_loose = (math.floor(corridor.bit_length() / 7) - j - 1)
                height += height_to_loose
                corridor = corridor >> X_DIM * height_to_loose
                break


height += math.ceil(corridor.bit_length() / X_DIM) -1
elapsed = time.time() - start

print_corridor(corridor)
print(f"After {rock_counter-1} rocks the tower has a height of {height}.")
print(f"{rock_counter-1} needed {elapsed} seconds.")

c_str = bin(corridor)[2:]
print("---Corridor---")
lines = [c_str[i-X_DIM:i][::-1] for i in range(len(c_str), X_DIM-1, -X_DIM)]
lines.append(c_str[0:len(c_str)%X_DIM][::-1])

block_counter = 0
for l in lines:
    if l == "1111111":
        block_counter += 1
print(f"Amount of blocking levels: {block_counter}")

