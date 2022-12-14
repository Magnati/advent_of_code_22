import enum
from typing import Tuple

from advent_of_code.utils import get_input

#lines = get_input("test_input.txt")
lines = get_input("input.txt")


class ActionLetters(enum.Enum):
    R = ['A', 'X']
    P = ['B', 'Y']
    S = ['C', 'Z']

    @classmethod
    def get_action(cls, letter: str):
        if letter in cls.R.value:
            return cls.R
        if letter in cls.P.value:
            return cls.P
        if letter in cls.S.value:
            return cls.S
        raise Exception("Wrong Letter")

    @classmethod
    def get_winning_action(cls, attack):
        if attack == cls.R:
            return cls.P
        if attack == cls.P:
            return cls.S
        if attack == cls.S:
            return cls.R

    @classmethod
    def get_loosing_action(cls, attack):
        if attack == cls.R:
            return cls.S
        if attack == cls.P:
            return cls.R
        if attack == cls.S:
            return cls.P

class ResultPoints(enum.Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0

LETTER_TO_RESULT = {
    'X': ResultPoints.LOSS,
    'Y': ResultPoints.DRAW,
    'Z': ResultPoints.WIN,
}

# Remember: I am right
PAIRS_TO_WIN = [
    (ActionLetters.S, ActionLetters.R),
    (ActionLetters.P, ActionLetters.S),
    (ActionLetters.R, ActionLetters.P),
]

ACTION_TO_POINTS = {
    ActionLetters.R: 1,
    ActionLetters.P: 2,
    ActionLetters.S: 3,
}

tuples = [tuple(elem.split(' ')) for elem in lines]
#tuples = [(ActionLetters.get_action(a), ActionLetters.get_action(b)) for a, b in tuples]
tuples = [(ActionLetters.get_action(a), LETTER_TO_RESULT[b]) for a, b in tuples]

results = []

# 2nd Part
for attack, needed_result in tuples:
    result = needed_result.value
    if needed_result == ResultPoints.DRAW:
        result += ACTION_TO_POINTS[attack]
    elif needed_result == ResultPoints.LOSS:
        result += ACTION_TO_POINTS[ActionLetters.get_loosing_action(attack)]
    elif needed_result == ResultPoints.WIN:
        result += ACTION_TO_POINTS[ActionLetters.get_winning_action(attack)]
    else:
        raise Exception("wrong result")

    results.append(result)

# 1st Part
# for attack, action in tuples:
#     result = ACTION_TO_POINTS[action]
#     if attack == action:
#         result += ResultPoints.DRAW.value
#     elif (attack, action) in PAIRS_TO_WIN:
#         result += ResultPoints.WIN.value
#     else:
#         result += ResultPoints.LOSS.value
#     results.append(result)

print(sum(results))
