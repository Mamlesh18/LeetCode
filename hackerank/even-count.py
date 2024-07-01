def even(n):
    count = {}
    for num in n:
        if num in count:
            count[num]+= 1
        else:
            count[num] = 1

    even_count = [num for num, i in count.items() if i%2==0]
    return even_count
n = list(map(int,input().split()))
print(even(n))