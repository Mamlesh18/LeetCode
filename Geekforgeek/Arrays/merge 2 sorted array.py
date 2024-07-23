def merge(nums1,nums2):
    sums = nums1 + nums2
    for i in range(0,len(sums)):
        for j in range(i+1,len(sums)):
            if sums[i] > sums[j]:
                sums[i],sums[j] = sums[j],sums[i]
    return sums

nums1 = [1,3,5,7]
nums2 = [0,2,6,8,9]
print(merge(nums1,nums2))