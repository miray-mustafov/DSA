def my_gcd(n1, n2):
    """ n1 must >= n2 to work so check before call gcd()"""
    remainder = n1 % n2
    if remainder == 0:
        return n2

    return my_gcd(n2, remainder)


def gcd(n1, n2):
    """Lector's implementation"""
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


num1 = 18
num2 = 48

print('my_gcd no >= check:', my_gcd(num1, num2))
print('gcd:', gcd(num1, num2))
# print('my_gcd:', my_gcd(num1, num2) if num1 >= num2 else my_gcd(num2, num1)) no need to check this
