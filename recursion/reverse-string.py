def reverse(strng):
    if len(strng) == 1:
        return strng
    return strng[-1]+reverse(strng[:-1])


print(reverse('nohtyp'),
      reverse('srellimppa'))