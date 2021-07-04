def gen(row_gen):
    for elem in row_gen:
        yield elem


def chain_loop(data):
    is_work = dict()
    ind = 0
    gens = [gen(obj) for obj in data]
    flag = 1
    for gener in data:
        is_work[ind] = 1
        ind = ind + 1
    while flag != 0:
        for i, gen1 in enumerate(gens):
            if is_work[i] != 0:
                try:
                    yield next(gen1)
                except(StopIteration):
                    is_work[i] = 0
        s = 0
        for key in is_work:
            s = s + is_work[key]
        if s == 0:
            flag = 0
