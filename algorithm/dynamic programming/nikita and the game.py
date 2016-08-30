t = int(raw_input())
global dic
dic = {}


def calculate_left_max(start, end):
    if end % 2 == 1 or end == 0 or start % 2 == 1:
        return 0
    else:
        mid = (end - start) / 2 + start
        if mid in dic:
            return max(1 + calculate_left_max(start, mid), 1 + calculate_left_max(mid, end))
        else:
            return 0


while t:
    t -= 1
    n = int(raw_input())
    array = map(int, raw_input().split(" "))
    sumi = 0
    for i in range(n):
        if array[i] == 0:
            pass
        else:
            sumi += array[i]
            dic[sumi] = 1
    if sumi == 0:
        print n - 1
    else:
        # print dic
        print calculate_left_max(0, sumi)
    dic.clear()



