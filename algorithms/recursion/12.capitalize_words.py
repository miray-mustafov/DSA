"""Write a recursive function called capitalizeWords. Given an array of words,
return a new array containing each word capitalized."""


def capitalizeWords(arr):
    word = ""
    try:
        for l in arr[0]:
            word = word + l.upper()
    except IndexError:
        return []
    return [word] + capitalizeWords(arr[1:])


words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)  # ['I', 'AM', 'LEARNING', 'RECURSION']
      )
