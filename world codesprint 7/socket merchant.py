n = int(raw_input())

values = [0]*101

colour = map(int,raw_input().split(" "))

for i in colour:
    values[i] += 1
ans = 0
for i in range(1,101):
    ans += values[i]/2
print ans
