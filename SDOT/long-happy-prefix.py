def happy(x):
    n = len(x)
    stack = []
    for i in range(n -1, 0 , -1):
        if x[:i] == x[-i:]:
            return x[:i]
    return ""

x = input()
print(happy(x))