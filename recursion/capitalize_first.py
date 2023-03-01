"""Write a recursive function called capitalizeFirst.
Given an array of strings, capitalize the first letter of each string in the array.
Example:
capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']"""


def capitalizeFirst(arr):
    try:
        word = arr[0].capitalize()
    except IndexError:
        return []
    return [word] + capitalizeFirst(arr[1:])


print(capitalizeFirst(['car', 'taco', 'banana']))  # ['Car','Taco','Banana']
