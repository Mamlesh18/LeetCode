def most(n):
    if len(n) == 0:
        return None
    area = 0
    for i in range(len(n)):
        for j in range(i +1, len(n)):
            area = max(area, min(n[j], n[i] * (j - i)))
    return area

n = list(map(int,input().split()))

print(most(n))


# def maxArea(A, Len):
#     area = 0
#     for i in range(Len):
#         for j in range(i + 1, Len):
#             # Calculating the max area
#             area = max(area, min(A[j], A[i]) * (j - i))
#     return area
#
#
# # Driver code
# a = [1, 5, 4, 3]
# b = [3, 1, 2, 4, 5]
#
# len1 = len(a)
# print(maxArea(a, len1))
#
# len2 = len(b)
# print(maxArea(b, len2))
# #



