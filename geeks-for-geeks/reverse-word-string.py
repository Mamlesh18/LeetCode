def rever(n):
    return " ".join(map(str,n[::-1]))

n = input().split()
print(rever(n))