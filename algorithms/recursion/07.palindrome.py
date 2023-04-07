def isPalindrome(strng):
    def reverse(s):
        if len(s) == 1:
            return s
        return s[-1] + reverse(s[:-1])

    if strng == reverse(strng):
        return True
    return False


print(isPalindrome('awesome'))  # false
print(isPalindrome('taccat'))  # true
print(isPalindrome('tacocat'))  # true
print(isPalindrome('amanaplanacanalpanama'))  # True
