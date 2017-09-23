def divide_by_zero(x, y):
    try:
        result = x / y
        print('result:', result)
    except ZeroDivisionError:
        print('Tried to divide by zero')
    print('Now here')


def sum_digits(s):
    """
    Assumes s is a string
    Returns the sum of the decimal digit in s
    For example, if s is 'a2b3c' it returns 5
    """
    total = 0

    for c in s:
        try:
            total += int(c)
        except ValueError:
            print('not an integer')

    print(total)


def square():
    while True:
        val = input('Enter an integer: ')
        try:
            val = int(val)
            print('The square of the number you entered is', val ** 2)
            break
        except ValueError:
            print(val, 'is not an integer')

def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg)
        try:
            return (val_type(val))
        except ValueError:
            print(val, error_msg)

def find_an_even(L):
    """
    Assumes L is a list of integers.
    Returns the first even number in L.
    Raises ValueError if L does not contain an even number.
    """
    even = None

    for i in L:
        if i % 2 == 0:
            even = i
            break

    if even == None:
        raise ValueError('Even number not found.')

    return even


def get_ratios(vect1, vect2):
    """
    Returns a list containing the meaningful values of vect1[i]/vect2[i]
    """
    length = len(vect1)
    ratios = []

    if length != len(vect2):
        raise ValueError('Array lengths are not equal.')

    for i in range(length):
        try:
            ratios.append(vect1[i] / vect2[i])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arguments')

    return ratios


if __name__ == '__main__':
    divide_by_zero(4, 2)
    divide_by_zero(4, 0)

    sum_digits('a2b3c')
    sum_digits('245')
    sum_digits('abc')

    # square()

    read_val(int, 'Enter an integer:', 'is not an integer')

    print(find_an_even([1, 3, 5, 11, 7, 2]))

    try:
        print(find_an_even([1, 3, 5]))
    except ValueError as msg:
        print(msg)

    try:
        print(get_ratios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
        print(get_ratios([], []))
        print(get_ratios([1.0, 2.0], [3.0]))
    except ValueError as msg:
        print(msg)

