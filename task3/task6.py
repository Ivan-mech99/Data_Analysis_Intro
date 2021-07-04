def brackets(n, token="", Lbr=0, Rbr=0):
    if Rbr + Lbr == 2*n:
        yield token
    if Lbr < n:
        cur_token = token + '('
        temp_Lbr = Lbr + 1
        temp_Rbr = Rbr
        yield from brackets(n, cur_token, temp_Lbr, temp_Rbr)
    if Lbr > Rbr:
        cur_token = token + ')'
        temp_Lbr = Lbr
        temp_Rbr = Rbr + 1
        yield from brackets(n, cur_token, temp_Lbr, temp_Rbr)


if __name__ == '__main__':
    print(*brackets(int(input())), sep="\n")
