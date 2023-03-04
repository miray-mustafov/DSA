def fib_sequence(n):
    if n == 0:
        return ""
    if n == 1:
        return "0"
    elif n == 2:
        return "0 1"
    else:
        sequence = fib_sequence(n - 1)
        last_number = int(sequence.split()[-1])
        second_last_number = int(sequence.split()[-2])
        result = sequence + f" {last_number + second_last_number}"
        return result


def fibonacci(n):
    assert 0 < n == int(n), 'Fibonacci number cannot be negative number or non integer.'
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def all_fibonacci(n):
    sequence = ''
    for i in range(1, n+1):
        sequence += f'{i}:, {fibonacci(i)} '
    return sequence

n = 7

print(fib_sequence(n))
print(fibonacci(n))
print(all_fibonacci(n))
