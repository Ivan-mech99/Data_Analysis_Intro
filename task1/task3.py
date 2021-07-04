num = float(input())
if num == 0:
    print('')
else:
    num = int(num*100)
    rub = num // 100
    cop = num % 100
    rb = dict()
    cp = dict()
    rb[10] = rub // 10
    rub = rub-10*rb[10]
    rb[5] = rub // 5
    rub = rub-5*rb[5]
    rb[2] = rub//2
    rub = rub-2*rb[2]
    rb[1] = rub
    cp[50] = cop//50
    cop = cop-50*cp[50]
    cp[10] = cop//10
    cop = cop-10*cp[10]
    cp[5] = cop//5
    cop = cop-5*cp[5]
    cp[1] = cop
    l1 = [10, 5, 2, 1]
    l2 = [50, 10, 5, 1]
    for elem in l1:
        if rb[elem] != 0:
            print("%5.2f\t%d" % (elem, rb[elem]))
    for elem in l2:
        if cp[elem] != 0:
            print("%5.2f\t%d" % ((elem/100), cp[elem]))
