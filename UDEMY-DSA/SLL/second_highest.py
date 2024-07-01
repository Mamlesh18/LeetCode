def second(arr):
    if len(arr) < 2:
        return None
    highest = arr[0]
    sec = float('-inf')

    for i in arr:
        if i > highest:
            sec = highest
            highest = i
        elif i > sec and i != highest:
            sec = i

    if sec == float('-inf'):
        return None
    else:
        return sec

input_arr = [1, 4, 7, 8, 4, 8, 1, 4, 9]
print("The second Highest number is  ->",second(input_arr))