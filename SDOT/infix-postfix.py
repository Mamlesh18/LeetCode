def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0
def inftopost(expression):
    stack = []
    postfix = ''
    for i in expression:
        if i.isalnum():
            postfix += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(i):
                postfix += stack.pop()
            stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix
n = input("enter the infix")
post = inftopost(n)
print("expression", post)