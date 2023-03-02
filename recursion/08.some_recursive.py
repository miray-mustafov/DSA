"""
Write a recursive function called someRecursive which accepts an array and a callback. The function returns true
if a single value in the array returns true when passed to the callback. Otherwise it returns false.

Examples:
someRecursive([1,2,3,4], isOdd) # true
someRecursive([4,6,8,9], isOdd) # true
someRecursive([4,6,8], isOdd) # false
"""


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    elif cb(arr.pop()):
        return True
    return someRecursive(arr, cb)


print(someRecursive([4, 9, 8, 6], isOdd))
print(someRecursive([1], isOdd))
print(someRecursive([10, 2], isOdd))
print(someRecursive([2], isOdd))
