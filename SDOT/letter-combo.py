def letter(digits):
    if not digits:
        return []

    mapping={ '1':'',
              '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}

    def backtrack(index,path):
        if index == len(digits):
            result.append(path)
            return
        for i in mapping[digits[index]]:
            backtrack(index+1,path+i)
    result = []
    backtrack(0,'')
    return sorted(result)

digits = input().strip()

result = letter(digits)
for i in result:
    print(i)