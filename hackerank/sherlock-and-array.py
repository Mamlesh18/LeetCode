def balancedSums(arr):

    for i in range(len(arr)-1):
        for j in range(0,len(arr),-1):
            if arr[i] + arr[i+1]:




n = list(map(int,input().split()))
print(balancedSums(n))
