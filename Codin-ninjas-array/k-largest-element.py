def k_largest(n,k):
    a = sorted(n)
    return ' '.join(map(str,a[-k:]))


t = int(input("enter testcases-> "))
for i in range(t):
    n = int(input("enter n "))
    k = int(input("enter k "))
    num = list(map(int,input().split()))
    print(k_largest(num,k))