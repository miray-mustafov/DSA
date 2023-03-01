def reverse(strng):
    if len(strng) == 1:
        return strng
    return strng[-1]+reverse(strng.rstrip())


print(reverse('nohtyp'),
      reverse('srellimppa'))