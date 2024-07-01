
def morganAndString(a, b):

    # Write your code here
    a+='z'
    b+='z'
    result = ""
    for i in range(len(a) + len(b) -2):
        if a<b:
            result+=a[0]
            a = a[1:]
        else:
            result+=b[0]
            b = b[1:]

    return result

a = input()
b = input()
print(morganAndString(a,b))