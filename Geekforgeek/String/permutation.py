from itertools import permutations
def strings(s):
    a = permutations(s)
    for i in a:
        print(''.join(i))

s = 'ABC'
print(strings(s))