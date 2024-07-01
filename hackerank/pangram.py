def pangrams(s):
    # Write your code here
    visited = set(s.lower())
    visited.discard(' ')
    if len(visited) ==  26:
        return 'pangram'
    else:
        return 'not pangram'


s = input()
print(pangrams(s))