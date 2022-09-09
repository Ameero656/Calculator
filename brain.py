


def basic_calculator():
    string = input('Equation (x +*/- x):')
    string = string.split()
    n1 = string[0]
    op = string[1]
    n2 = string[2]

    if op == '+':
        return n1+n2
    if op == '-':
        return n1-n2
    if op == '*':
        return n1*n2
    if op == '/':
        return n1/n2    