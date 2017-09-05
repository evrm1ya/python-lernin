def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_palindrome(word):
    if word == '' or len(word) == 1:
        return True

    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:-1])


def is_odd(x):
    return x % 2 != 0

def power(x, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / power(x, n * -1)

    if is_odd(n):
        return x * power(x, n - 1)

    y = power(x, n / 2)
    return y * y


if __name__ == '__main__':
    print(factorial_iterative(5))
    print(factorial(0))
    print(factorial(5))
    #print(factorial(200))

    print('rotor is palindrome', is_palindrome('rotor'))
    print('motor is palindrome', is_palindrome('motor'))

    print(power(2.0, 0))
    print(power(3.0, 2))
    print(power(5.0, 3))
    print(power(2.0, -2))
    print(power(5.0, -3))
    print(power(2.0, 4))
    print(power(2.0, -4))
