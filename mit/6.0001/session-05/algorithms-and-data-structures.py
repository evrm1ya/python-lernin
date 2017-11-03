# python's linear search
def linear_search(e, L):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False


def ascending_search(e, L):
    """Assumes L is a list, the elements of which
    are in ascending order.

    Returns True if e is in L and False otherwise"""

    for i in range(len(L)):
        if L[i] == e:
            return True

        if L[i] > e:
            return False

    return False


# book example
def b_search(L, e):
    """Assumes L is a list, the elements of which
    are in ascending order.

    Returns True if e is in L and False otherwise."""

    def search(L, e, low, high):
        # Decrements high - low
        if high == Low:
            return L[low] == e

        mid = (low + high) // 2

        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return search(L, e, low, mid - 1)
        else:
            return search(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return search(L, e, 0, len(L) - 1)


# shorter
def binary_search(e, L):
    length = len(L)
    print('\nlength', length)

    if length == 0:
        return False

    high = length - 1
    print('high', high)
    avg = high // 2
    print('avg', avg)

    if L[avg] == e:
        return True

    if L[avg] < e:
        return binary_search(e, L[avg + 1:])
    else:
        return binary_search(e, L[:high - avg])



if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]

    print('searching...', binary_search(3, L))

    print('searching...', binary_search(2, L))

    print('searching...', binary_search(1, L))

    print('searching...', binary_search(4, L))

    print('searching...', binary_search(5, L))

    print('searching...', binary_search(6, L))

