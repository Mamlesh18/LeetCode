def merge(list1, list2):
    stack = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            stack.append(list1[i])
            i += 1
        else:
            stack.append(list2[j])
            j += 1
    while i < len(list1):
        stack.append(list1[i])
        i += 1
    while j < len(list2):
        stack.append(list2[j])
        j += 1
    a = len(stack)
    if a % 2 != 0:
        b = a//2
        print(stack[b])
    else:
        b = a // 2
        c = stack[b-1]
        d = stack[b]
        e = (c + d)/2
        print(e)




lis1 = list(map(int, input().split()))
lis2 = list(map(int, input().split()))
merge(lis1, lis2)
