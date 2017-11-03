def int_to_str(i):
    """Assumes i is a nonnegative int
    Returns a decimal string representation of i"""

    digits = '0123456789'

    if i == 0:
        return '0'

    result = ''

    # O(log(i))
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10

    return result


# O(log(n)) + O(log(n)) => O(log(n))
def add_digits(n):
    """Assumes n is a nonnegative int
    Returns the sum of the digits in n"""

    # O(log(n))
    string_rep = int_to_str(n)

    val = 0

    # O(len(string_rep))
    # O(log(n)) times
    for c in string_rep:
        val += int(c)

    return val

# O(len(s))
def add_digits_linear(s):
    """Assumes s is a str. Each character of which
    is a decimal digit.
    Returns an int that is the sum of the digits in s"""

    val = 0

    for c in s:
        val += int(c)

    return val

# O(x)
def factorial(x):
    """Assumes x is a positive int
    Returns x!"""

    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


# O(len(l1) * len(l2))
def is_subset(l1, l2):
    """Assumes l1 and l2 are lists.
    Returns True if each element in l1 is also in l2
    and False otherwise."""

    for e1 in l1:
        matched = False

        for e2 in l2:
            if e1 == e2:
                matched = True
                break

        if not matched:
            return False

    return True


def get_binary_rep(n, num_digits):
    """Assumes n and num_digits are non-negative ints
    Returns a str of length num_digits that is a binary
    representation of n."""

    result = ''

    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    if len(result) > num_digits:
        raise ValueError('Not enough digits')

    for i in range(num_digits - len(result)):
        result = '0' + result

    return result


def gen_powerset(L):
    """Assumes L is a list
    Returns a list of lists that contains all possible
    combinations of the elements of L. E.g, if L is
    [1, 2] it will return a list with elements
    [], [1], [2], and [1, 2]."""

    powerset = []

    for i in range(0, 2 ** len(L)):
        bin_str = get_binary_rep(i, len(L))
        subset = []

        for j in range(len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])

        powerset.append(subset)

    return powerset


if __name__ == '__main__':
    print(int_to_str(20))
    print(int_to_str(21))
    print(int_to_str(101))

    print(add_digits(2048))