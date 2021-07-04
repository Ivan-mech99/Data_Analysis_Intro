def solution1(word):
    return [letter*4 for letter in word]


def solution2(word):
    return [(pos+1)*letter for pos, letter in enumerate(word)]


def solution3(numlist):
    return [number for number in numlist if
            ((number % 5 == 0) or (number % 3 == 0))]


def solution4(list2):
    return [elem for list1 in list2 for elem in list1]


def solution5(n):
    return [(x, y, z) for z in range(5, n+1) for y in range(1, z) for x
            in range(1, y) if (x*x+y*y == z*z)]


def solution6(arg):
    return [[arg0 + arg1 for arg1 in arg[1]]
            for arg0 in arg[0]]


def solution7(mat):
    return [[row[col] for row in mat] for col in range(0, len(mat[0]))]


def solution8(arg):
    return [[int(num) for num in string.split()] for string in arg]


def solution9(arg):
    return {chr(97+i): i * i for i in arg}


def solution10(wordlist):
    return {word.capitalize() for word in wordlist if (len(word) > 3)}


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
