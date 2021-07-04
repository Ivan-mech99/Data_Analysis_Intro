N = int(input())
words = []
for i in range(0, N):
    words.append(input())
while len(words) > 0:
    words_to_rem = []
    words_to_rem.append(words[0])
    if len(words) > 1:
        sd1 = dict()
        for elem in words[0]:
            if elem not in sd1:
                sd1[elem] = 1
        else:
            sd1[elem] = sd1[elem]+1
        for i in range(1, len(words)):
            broke = 0
            sd2 = dict()
            for elem in words[i]:
                if elem not in sd2:
                    sd2[elem] = 1
                else:
                    sd2[elem] = sd2[elem]+1
            for key in sd2:
                if key not in sd1:
                    broke = -1
                else:
                    if sd2[key] > sd1[key]:
                        broke = -1
            if broke == 0:
                words_to_rem.append(words[i])
        for i in range(0, len(words_to_rem)):
            words.remove(words_to_rem[i])
        if len(words_to_rem) > 1:
            for i in range(0, len(words_to_rem)-1):
                print(words_to_rem[i], end=' ')
            print(words_to_rem[len(words_to_rem)-1])
        else:
            print(words_to_rem[0])
    else:
        print(words[0])
        words = []
