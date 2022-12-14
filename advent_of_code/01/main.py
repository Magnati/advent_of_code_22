

with open("input.txt") as input_file:
    lines = input_file.readlines()

# only 2nd part still existing
highest_tripple = [0, 0, 0]
current_max = 0
for line in lines:
    if line != '\n':
        current_max += int(line.strip('\n'))
    else:
        minimum = min(highest_tripple)
        if current_max > minimum:
            highest_tripple[highest_tripple.index(minimum)] = current_max
        current_max = 0

print(sum(highest_tripple))
