import sys
def palindromes(S):
    results = []
    S_length = len(S)
    for idx, char in enumerate(S):
        results.append(char)

        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < S_length and S[start] == S[end]:
            results.append(S[start:end+1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < S_length and S[start] == S[end]:
            results.append(S[start:end+1])
            start -= 1
            end += 1

    return list(results)

def pow_mod(a, x, y, z):
    "Calculate (x ** y) % z efficiently."
    a=a%z
    number = 1
    # print type(a)
    # print a
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    #return ((a%z)*number)%z
    number *=a
    number %=z
    return number


#print pow_mod(3,2,4,5)


def calculateFun(s):
    m=1000000007
    l=len(s)
    f=0
    a=100001
    for index,i in enumerate(s):
        # print i
        # print a
        # print l-1-index
        # print m
        f+=pow_mod(ord(i),a,l-1-index,m)%m
    return f%m




n,q=map(int,raw_input().split(" "))
S=raw_input()
S= sorted(palindromes(S))
# print S
# sys.exit()
while q:
    q -=1
    i = int(raw_input())
    if i<=len(S):
        #print S[i-1]
        print calculateFun(S[i-1])
    else:
        print -1

