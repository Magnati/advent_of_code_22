import enum
import string
from typing import List

from advent_of_code.utils import get_input

lines = get_input("test_input.txt")
lines = get_input("input.txt")

x_dim = len(lines[0])
y_dim = len(lines)

if x_dim != y_dim:
    raise Exception("Uhoh, no square")

grid = [[] for _ in range(x_dim)]
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x].append(int(c))

def print_grid(grid: List[List[int]]):
    result = ''
    for y in range(x_dim):
        for x in range(x_dim):
            result += str(grid[x][y])
        result += "\n"
    print(result)

print_grid(grid)

visible = [[False for i in range(x_dim)] for _ in range(x_dim)]
for y in range(x_dim):
    for x in range(x_dim):
        if x == 0 or y == 0 or x == x_dim-1 or y == y_dim-1:
            visible[x][y] = True

for x in range(1, x_dim-1):
    for y in range(1, x_dim-1):
        height = grid[x][y]
        east = west = north = south = True
        for i in range(x):
            if grid[i][y] >= height:
                east = False
                break
        for i in range(x+1, x_dim):
            if grid[i][y] >= height:
                west = False
                break
        for j in range(y):
            if grid[x][j] >= height:
                north = False
                break
        for j in range(y+1, x_dim):
            if grid[x][j] >= height:
                south = False
                break
        if any([north, south, east, west]):
            visible[x][y] = True

print("PART ONE")
print_grid(visible)
count = 0
for line in visible:
    count += line.count(True)
print(f"{count} trees are visible")


sight = [[0 for i in range(x_dim)] for _ in range(x_dim)]
for x in range(x_dim):
    for y in range(x_dim):
        height = grid[x][y]
        east = west = north = south = 0
        for i in range(x-1,-1,-1):
            east += 1
            if grid[i][y] >= height:
                break
        for i in range(x+1, x_dim):
            west += 1
            if grid[i][y] >= height:
                break
        for j in range(y-1,-1,-1):
            north += 1
            if grid[x][j] >= height:
                break
        for j in range(y+1, x_dim):
            south += 1
            if grid[x][j] >= height:
                break
        sight[x][y] = east * west * north * south

print("PART TWO")
print_grid(sight)
max_sight = max([max(l) for l in sight])
print(f"The max sight is {max_sight} at:")

for x in range(x_dim):
    for y in range(x_dim):
        if sight[x][y] == max_sight:
            print(f"({x}:{y})")
