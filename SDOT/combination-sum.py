def combination(x, y):
    def backtrack(s, target, path):
        if target == 0:
            result.append(path[:])  # Append a copy of the path
            return
        if target < 0:
            return
        for i in range(s, len(x)):
            backtrack(i, target - x[i], path + [x[i]])

    x.sort()  # Sort the array of distinct integers
    result = []
    backtrack(0, y, [])
    return result

x = list(map(int, input().split()))
y = int(input())
print(combination(x, y))
