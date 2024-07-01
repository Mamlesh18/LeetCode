def pare(n):
    stack = []
    stack2 = []
    for i in n:
        if i == '(':
            stack.append(i)
        else:
            stack2.append(i)
    return (min(len(stack),len(stack2))) * 2
n = input()
print(pare(n))