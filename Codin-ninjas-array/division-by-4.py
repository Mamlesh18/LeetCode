def division(n):
    results = []
    for num in n:
        if num % 4 == 0:
            results.append(num // 4)
        else:
            results.append(-1)
    return results

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(division(numbers))
