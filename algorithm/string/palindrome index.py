t = int(raw_input())


def pal_check(S):
    n = len(S)
    for i in range((len(S) + 1) / 2):
        if S[i] == S[n - i - 1]:
            pass
        else:
            return 0
    return 1


while t:
    t -= 1
    S = list(raw_input())
    n = len(S)
    flag = 0
    for i in range((n + 1) / 2):
        if S[i] != S[n - 1 - i]:
            if pal_check(S[i:n - i - 1]):
                print n - i - 1
                flag = 1
                break
            elif pal_check(S[i + 1:n - i]):
                print i
                flag = 1
                break

    if flag == 0:
        print -1

