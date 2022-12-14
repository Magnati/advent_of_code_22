from advent_of_code.utils import get_input

lines = get_input("test_input.txt")
lines = get_input("input.txt")

# scan towers
head = True
towers = []
moves = []
for line in lines:
    if head:
        if '[' in line:
            towers.append(line)
        else:
            tower_ids = [int(x) for x in line.split(' ') if x]
            head = False
    else:
        if line:
            moves.append(line)

tower_cnt = tower_ids[-1]
print(towers)
print(tower_cnt)
print(moves)
stacks = [[] for _ in range(tower_cnt)]


def get_move_tripple(line):
    return tuple([int(x) for x in line.split(' ') if x.isnumeric()])

move_tripples = [get_move_tripple(move) for move in moves]
print(move_tripples)

def create_stacks(lines, stacks, chunk=3):
    for line in lines[::-1]:
        test2 = line[1::4]
        for i in range(tower_cnt):
            if test2[i] != ' ':
                stacks[i].append(test2[i])
    return stacks

stacks = create_stacks(towers, stacks)
print(stacks)

def do_moves(move_tripples, stacks):
    move_count = 0
    for count, _from, _to in move_tripples:
        move_count += 1
        for _ in range(count):
            stacks[_to-1].append(stacks[_from-1].pop())

        print(str(move_count) + ': ' + str(stacks))
    return stacks

#stacks = do_moves(move_tripples, stacks)
#print(stacks)

def do_moves_2(move_tripples, stacks):
    pass


for slice, _from, _to in move_tripples:
    stacks[_to-1] += stacks[_from-1][-slice:]
    stacks[_from - 1] = stacks[_from-1][:-slice]

print(stacks)
print("".join([s.pop() for s in stacks]))

