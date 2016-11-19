t =int(raw_input())
global modulus
modulus = 1000000007

def pow_mod(x, y, z):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def modMuliple(lis):
    modi = int(lis[0])%modulus
    for i in lis[1:]:
        modi=(modi*(int(i)%modulus))%modulus
    return modi
def calculatePowerExpres(expression):
    expression = expression.split('^')
    value = pow_mod(int(expression[0]),int(expression[1]),modulus)
    for i in expression[2:]:
        value = pow_mod(value,int(i),modulus)
    return value

def calculate(expression):
    if expression[0]=='*' or expression[-1]=='*':
        return 'Syntax Error'

    expression = expression.replace('**','^')
    if '^^' in expression or '*^' in expression or '^*' in expression:
        return 'Syntax Error'
    expression = expression.split('*')
    #print expression
    for index,item in enumerate(expression):
        if '^' in item:
            expression[index]=calculatePowerExpres(item)
    #print expression
    return modMuliple(expression)

while t:
    t -= 1
    print calculate(raw_input())