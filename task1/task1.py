from collections import OrderedDict
n = int(input())
list_1 = input().split()
list_1 = list(map(int, list_1))
res = list(OrderedDict.fromkeys(list_1))
for i in range(0, len(res)-1):
    print(res[i], end=' ')
print(res[len(res)-1])
print(len(list_1)-len(res))
