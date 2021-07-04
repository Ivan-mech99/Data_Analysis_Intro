N = int(input())
unord = []
sent = input().split()
for elem in sent:
    sum_num = 0
    for nb in elem:
        sum_num = sum_num+int(nb)
    unord.append((sum_num, int(elem)))
res = sorted(unord, key=lambda x: (x[0], x[1]))
for elem in res:
    print(elem[1], end=" ")
