def rever(nums):
    result = ''
    temp=''
    right = len(nums) -1
    while right >= 0:
        if nums[right] == '.':
            result+=temp[::-1] + '.'
            temp =''
        else:
            temp += nums[right]
        right-=1
    result+=temp[::-1]
    return result



S = 'i.like.this.program.very.much'
print(rever(S))