N = int(input())
words = []
for i in range(0, N):
    words.append(input())
bigd = dict()
for elem in words:
    hold = sorted(elem)
    hold1 = ''.join(str(x) for x in hold)
    if hold1 not in bigd:
        bigd[hold1] = []
        bigd[hold1].append(elem)
    else:
        bigd[hold1].append(elem)
for ilt in bigd:
    s1 = len(bigd[ilt])
    for j in range(0, s1-1):
        print(bigd[ilt][j], end=' ')
    print(bigd[ilt][s1-1])
