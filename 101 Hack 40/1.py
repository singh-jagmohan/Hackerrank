# Enter your code here. Read input from STDIN. Print output to STDOUT

t= int(raw_input())
heights = map(int,raw_input().split(' '))
m = int(raw_input())
lasers = map(int,raw_input().split(' '))
lasers = sorted(lasers)

j = 0
sumi =0
for i in range(t+1):
    # print "lasers",
    # print lasers[j]
    # print "heights",
    # print  heights[i]
    if i == lasers[j]-1:
        j += 1
    if j == m:
        sumi += sum(heights[i:])
        break
    if heights[i] >= lasers[j]-i -1:
        sumi += lasers[j] - i -1
    else:
        sumi += heights[i]
    # print sumi
print sumi



