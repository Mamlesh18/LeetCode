def sock(n,arr):
    dicts = {}
    for i in arr:
        if i in dicts:
            dicts[i]+=1
        else:
            dicts[i] = 1
    count = sum(value//2 for value in dicts.values())
    return count


n = int(input())
arr = list(map(int,input().split()))
print(sock(n,arr))