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

def is_palindrome(s):
    """
    Assumes s is a str
    Returns True if letters in s form a palindrome;
        False otherwise. Non-letters and capitalization
        are ignored.
    """
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

print(is_palindrome('dogGod'))
print(is_palindrome('doGood'))

def test_is_palindrome(s):
    """
    Assumes s is a str
    Returns True if letters in s form a palindrome;
        False otherwise. Non-letters and capitalization
        are ignored.
    """
    print('Try', s)
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def is_pal(s):
        print(' is_pal called with', s)
        if len(s) <= 1:
            print(' About to return True from base case')
            return True
        else:
            answer = s[0] == s[-1] and is_pal(s[1:-1])
            print(' About to return', answer, 'for', s)
            return answer

    return is_pal(to_chars(s))

print(test_is_palindrome('dogGod'))
print(test_is_palindrome('doGood'))

