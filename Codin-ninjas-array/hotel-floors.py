def hotel(N):
    a = str(N)
    count= 0
    for i in N:
        if i.startswith('+'):
            count += 1
    return count


user_input = input("Enter string values separated by space: ")

n = user_input.split()

print(hotel(n))
