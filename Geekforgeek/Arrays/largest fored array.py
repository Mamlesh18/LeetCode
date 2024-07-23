from functools import cmp_to_key
def large(nums):
    def comp(n,m):
        if n+m > m+n:
            return -1
        else:
            return 1
    arr = sorted(nums,key= cmp_to_key(comp))
    return ''.join(arr)
nums = ["3", "30", "34", "5", "9"]
print(large(nums))