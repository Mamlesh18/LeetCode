def pair(x,y):
    count = 0
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            if x[i] ** y[j] > y[j] ** x[i]:
                count+=1
    return count
x = [2,3,4,5]
y = [1,2,3]
print(pair(x,y))