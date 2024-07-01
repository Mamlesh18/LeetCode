from sys import maxsize

def contiguos_array(n):

    if len(n) == 0:
        return None

    maxsum = -1e8

    for i in range(0,len(n)):
        curr = 0
        for j in range(i,len(n)):
            curr = curr +n[j]
            if (curr>maxsum):
                maxsum = curr
    return maxsum




n = list(map(int,input().split()))

print(contiguos_array(n))