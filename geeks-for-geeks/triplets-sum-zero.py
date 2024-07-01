def triplets(n):
    if len(n) == 0:
        return None

    for i in range(0, len(n)-2):
            for j in range(i + 1, len(n)-1):
                for k in range(j + 1, len(n)):
                    if n[i] + n[j] + n[k] == 0:
                        print(n[i], n[j], n[k])

    return "No"

n = list(map(int,input().split(',')))
print(triplets(n))