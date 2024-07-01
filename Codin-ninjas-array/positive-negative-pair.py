def pos(n):
    stack = []
    for i in range(0, len(n)):
        for j in range(i):
            if n[i] + n[j] == 0:
                stack.append((min(n[i], n[j]), max(n[i], n[j])))

    stack.sort(key=lambda x: (abs(x[0]), abs(x[1])))

    return stack

n = list(map(int, input().split()))
result = pos(n)

# Output the pairs without brackets and separated by space
output_pairs = []
for pair in result:
    output_pairs.extend(pair)

print(*output_pairs)
