# factorial
# 1! = 1
# (n + 1)! = (n + 1) * n!

def factI(n):
    """
    Assumes n is an int > 0
    Returns n!
    """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

print(factI(5))

def factR(n):
    if n == 1:
        return n
    else:
        return n * factR(n - 1)

print(factR(5))

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def test_fib(n):
    for i in range(n + 1):
        print('fib of', i, '=', fib(i))

test_fib(3)
