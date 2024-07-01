n = int(input("Enter the temp of each day"))
count = 0
for i in range(1,n+1):
    a = int(input("days" + str(i) + "today temp"))
    count += a
avg = round(count / n,2)
print(str(avg))
