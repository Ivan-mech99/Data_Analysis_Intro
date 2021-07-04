from collections import defaultdict


def smartdict_nan(key):
    return 10 * key


N = 10

smartdict = {}
for key in range(N):
    val = defaultdict(lambda key1=key: smartdict_nan(key1))
    smartdict[key] = val

"""
Изначальный код работал неверно, поскольку когда мы обращались по несуществующему ключу, вызывалась лямбда функция
lambda: smartdict_nan(key), в локальной области видимости которой не было переменной key. Программа искала эту
переменную по правилу LEGB: Local -> Enclosed -> Global -> Built-in, и находила ее в глобальной области видимости.
Но там после прохода по циклу она уже успела стать равной 9. Я исправил это, создав локальную переменную key1 в области
видимости лямбда функции, и присваивая ей на каждой итерации key, подавая ее (key1) затем в smartdict_nan.
"""
