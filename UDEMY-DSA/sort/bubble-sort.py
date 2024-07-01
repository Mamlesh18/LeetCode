def bubblesort(clist):
    for i in range(0,len(n) -1):
        for j in range(len(n) -i -1):
            if n[j] > n[j+1]:
                n[j] , n[j+1] = n[j+1], n[j]
    print(clist)

n = list(map(int,input().split()))
bubblesort(n)

# it iteraties each one from the first ,
# if it detect something greater than
# the element that it is iterating, it
# will take that element and start iterating
# Time complexity o(n^2)