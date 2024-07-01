def build(a,b,s):
    result = ""
    stack = []
    for i in range(len(s)-1):
        if s not in result:
            stack.append(a)
            result +=s[0]
          
            s = s[1:]
        elif s in result:
            stack.append(b)
            result+=s[0]
            s = s[1:]
    return sum(stack),result
a = int(input())
b = int(input())
s = input()
print(build(a,b,s))