n, k = map(int,raw_input().split(' '))
p = map(float,raw_input().split(' '))
x = map(float,raw_input().split(' '))
y = map(float,raw_input().split(' '))
values = []
for i in range(n):
    values.append(p[i]*x[i]-(1-p[i])*y[i])
sumi = 0.0
values = sorted(values)
for i in range(k):
    if sumi<sumi+values[n-1-i]:
        sumi +=values[n-1-i]
    else:
        break
print "%.2f"%sumi

