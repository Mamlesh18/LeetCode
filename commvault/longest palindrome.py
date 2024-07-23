def long(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    longest_palindrome = ''

    for left in range(len(s)):
        for right in range(left, len(s)):
            temp = s[left:right + 1]
            if is_palindrome(temp) and len(temp) > len(longest_palindrome):
                longest_palindrome = temp

    return longest_palindrome


s = 'forgeeksskeegfor'
print(long(s))
