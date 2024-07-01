def sherlockAndAnagrams(s):
    s += 'z'
    count = 0
    for i in enumerate(s):
        for j in range(i, len(s), -1):
            if s[i:] == s[:j]:

                count += 1
    return count

n = input()
print(sherlockAndAnagrams(n))