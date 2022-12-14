from advent_of_code.utils import get_input

lines = get_input("test_input.txt")
lines = get_input("input.txt")

comps = [(line[:len(line)//2], line[len(line)//2:]) for line in lines]

def char_to_score(c):
    result = ord(c)-96
    if result < 1:
        result += 58
    return result

results = []
for left, right in comps:
    for c in left:
        if c in right:
            results.append(char_to_score(c))
            break

print("PART ONE")
print(results)
print(sum(results))

groups = list(zip(lines[::3],lines[1::3],lines[2::3]))

results = []
for a, b, c in groups:
    for c_a in a:
        if c_a in b and c_a in c:
            results.append(char_to_score(c_a))
            break

print("PART TWO")
print(results)
print(sum(results))
