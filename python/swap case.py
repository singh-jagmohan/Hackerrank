s = raw_input()
newS = ''
for i in s:
    if i.isupper()==True:
        newS +=i.lower()
    elif i.islower()==True:
        newS += i.upper()
    else:
        newS += i
print newS