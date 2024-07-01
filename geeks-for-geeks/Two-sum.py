def sumofpair(n,k):
    print(len(n))
    for i in range(0,len(n)):
        for j in range(i):
            if n[i] + n[j] == k:
                return "Yes"
    return "No"

n = list(map(int,input().split()))
k = int(input())

print("answer -> ",sumofpair(n,k))