import enum

from advent_of_code.utils import get_input

lines = get_input("test_input.txt")
#lines = get_input("input.txt")

class Comands(enum.Enum):
    LS = 'ls'
    CD = 'cd'

output = []
ls = False
for line in lines:
    if ls:
        output.append(line)
    else:
        if line.startswith('$'):
            if ls:
                ls = False
                # interpret result
            splited = line.split(' ')
            if len(splited) == 3:
                dollar, comand, parameter = splited
            elif len(splited) == 2:
                dollar, comand = splited
            else:
                raise Exception("")
            if comand == 'ls':
                ls = True
            elif comand == 'cd':
                pass
            else:
                raise Exception("unknown command")
        else:
            pass
