from advent_of_code.utils import get_input

#line = get_input("test_input.txt")[0]
line = get_input("input.txt")[0]

monitor = ''
end_index = -1
for i, c in enumerate(line):
    if c in monitor:
        monitor = monitor[monitor.index(c)+1:]

    monitor += c
    if len(monitor) == 14:
        end_index = i+1
        break

print(monitor)
print(end_index)


