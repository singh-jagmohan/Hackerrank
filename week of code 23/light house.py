n = int(raw_input())
landscape = []
for i in range(n):
    landscape.append(raw_input())
maximum = (n -1) / 2
if n%2==1:
    center = [[maximum,maximum]]
else:
    center = [[maximum,maximum+1],[maximum,maximum],[maximum+1,maximum],[maximum+1,maximum+1]]


def calculate(center,radius):
    return True


radius = maximum
while 1:
    if calculate(center,radius):
        print radius
    radius -= 1



