from functools import cmp_to_key
def larger(arr):
    def compare(x,y):

        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
    sorting = sorted(arr,key = cmp_to_key(compare))
    result = ''.join(sorting)

    if result[0] == '0':
        return '0'
    return result
arr1 = ["3", "30", "34", "5", "9"]
arr2 = ["54", "546", "548", "60"]

print(larger(arr1))  # Output: "9534330"
print(larger(arr2))  # Output: "6054854654"