# Enter your code here. Read input from STDIN. Print output to STDOUT
old = map(int, raw_input().split(" "))
new = map(int, raw_input().split(" "))
count = 0
for index, item in enumerate(old):
    maxi = max(item, new[index])
    mini = min(item, new[index])
    val1 = abs(item - new[index])
    val2 = abs(mini - 0) + abs(9 - maxi) + 1
    count += min(val1, val2)
print count
