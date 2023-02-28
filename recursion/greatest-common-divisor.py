def my_gcd(n1, n2):
    """ n1 must >= n2 to work so check before call gcd()"""
    remainder = n1 % n2
    if remainder == 0:
        return n2

    return my_gcd(n2, remainder)

num1 = 48
num2 = 18

print('my_gcd:', my_gcd(num1, num2) if num1 >= num2 else my_gcd(num2, num1))
