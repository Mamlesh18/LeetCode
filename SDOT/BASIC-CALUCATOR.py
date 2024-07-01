def basic(expression):
    stack = []
    num = 0
    last_op = '+'

    for i, char in enumerate(expression):
        if char.isdigit():
            num = int(char)

        if not char.isdigit() and char != ' ' or i == len(expression) -1:
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    stack.append(stack.pop() * num)
                elif last_op == '/':
                    stack.append(int(stack.pop() / num))
                last_op = char
                num = 0
    return sum(stack)

ele = input()
print(basic(ele))
