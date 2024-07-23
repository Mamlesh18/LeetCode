def strings(s1,s2):
    n1 = len(s1)
    n2 = len(s2)


    result = 0
    for i in range(n1):
        current = 0
        k = i
        for j in range(n2):
            if k < n1 and s1[k] == s2[j]:
                current+=1
                k+=1
                result = max(result,current)
            else:
                current = 0
                k = i
    return result



    return len(result)

s1 = 'ROMANINROMES'
s2 = 'XMANBATANINROMY'

print(strings(s1,s2))
