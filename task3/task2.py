import re
from functools import reduce


def solution1(arg):
    return list(map(lambda y: int(y),
                (list(map(lambda x: re.sub(r'[.,-]', "",
                 x.strip()[::-1]), arg)))))


def solution2(arg):
    return list(map(lambda x: x[0]*x[1], list(arg)))


def solution3(arg):
    return list(filter(lambda x: x % 6 not in [1, 3, 4], arg))


def solution4(arg):
    return list(filter(lambda x: x, arg))


def solution5(rooms):
    list(map(lambda rooms: rooms.update
         ({"square": rooms["width"]*rooms["length"]}), rooms))
    return rooms


def solution6(rooms):
    return list(map(lambda room: dict([*room.items(),
                    ("square", room["length"] * room["width"])]), rooms))


def solution7(arg):
    return reduce(lambda x, y: x.intersection(y), arg)


def solution8(arg):
    return reduce(lambda x, y: dict([*x.items(),
                  (y, x[y]+1 if y in x else 1)]), arg, dict())


def solution9(arg):
    return list(map(lambda x: x['name'],
                list(filter(lambda x: x['gpa'] > 4.5, arg))))


def solution10(arg):
    return list(filter(lambda num: reduce(lambda num, new_dig: -(int(num) -
                int(new_dig)), num) == 0, arg))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
