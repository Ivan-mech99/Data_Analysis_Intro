args = input().split()
N = int(args[0])
K = int(args[1])
if K == 0:
    print(K)
else:
    res = 0
    for i in range(1, K+1):
        hold = int(i*args[0])
        res = res+hold
    print(res)
