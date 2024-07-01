def pickingNumbers(a):
    max_length = 0
    frequency = [0] * len(a)  # As per constraints, the array elements range from 0 to 100

    for num in a:
        frequency[num] += 1

    for i in range(1, len(a)):
        max_length = max(max_length, frequency[i] + frequency[i - 1])

    return max_length


n = list(map(int,input().split()))
print(pickingNumbers(n))