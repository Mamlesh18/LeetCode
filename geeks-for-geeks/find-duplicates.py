def duplicates(n):
    # visi = set(n)
    #
    # return visi

    duplicates = []

    for i in n:
        if i not in duplicates:
            duplicates.append(i)
    return " ".join(map(str,duplicates))



n = list(map(int,input().split()))

print(duplicates(n))