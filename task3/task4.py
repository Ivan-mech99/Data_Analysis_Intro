import functools


def counter(func1):
    func1.ncalls = 0
    func1.rdepth = 0
    func1.cur_pos = 0

    @functools.wraps(func1)
    def wrapper(*args, **argv):
        if wrapper.cur_pos == 0:
            wrapper.ncalls = 0
            wrapper.rdepth = 0
        wrapper.ncalls = wrapper.ncalls + 1
        wrapper.cur_pos = wrapper.cur_pos + 1
        func2 = func1(*args, **argv)
        if wrapper.cur_pos > wrapper.rdepth:
            wrapper.rdepth = wrapper.cur_pos
        wrapper.cur_pos = wrapper.cur_pos - 1
        return func2
    return wrapper
