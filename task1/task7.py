import sys


def prepare_q(left, right, size):
    res = dict()
    cur = left
    while cur + size < right:
        cur = cur + size
        res[cur] = 0
    res[right] = 0
    return res


def ask(quest):
    for key in quest:
        print("? {}".format(key))
    print("+")
    sys.stdout.flush()


def get_ans(quest):
    for key in quest:
        quest[key] = int(input())


def new_borders(borders, quest):
    for key in quest:
        if quest[key] == 1 and borders[1] > key - 1:
            borders[1] = key - 1
        if quest[key] == 0 and borders[0] < key:
            borders[0] = key


borders = dict()
borders[0] = 1
borders[1] = 100000
sizes = [10000, 1000, 100, 10, 1]
for size in sizes:
    quest = prepare_q(borders[0], borders[1], size)
    ask(quest)
    get_ans(quest)
    new_borders(borders, quest)
print("! {}".format(borders[0]))
