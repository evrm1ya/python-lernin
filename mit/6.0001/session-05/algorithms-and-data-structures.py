import random

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
    mid = high // 2
    print('mid', mid)

    if L[mid] == e:
        return True

    if L[mid] < e:
        return binary_search(e, L[mid + 1:])
    else:
        return binary_search(e, L[:high - mid])


def do_some_binary_searchin():
    L = [1, 2, 3, 4, 5]

    print('searching...', binary_search(3, L))

    print('searching...', binary_search(2, L))

    print('searching...', binary_search(1, L))

    print('searching...', binary_search(4, L))

    print('searching...', binary_search(5, L))

    print('searching...', binary_search(6, L))


def selection_sort(L):
    """Assumes that L is a list of elements that can
    be compared using >.

    Sorts L in ascending order."""

    suffix_start = 0

    while suffix_start != len(L):
        print('suffix iteration:', suffix_start)

        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                print(L)

                log = 'Moving {} at index {} to index {}'.format(L[i], i, suffix_start)
                print(log)

                L[suffix_start], L[i] = L[i], L[suffix_start]

                print(L)
                print('-------\n')

        suffix_start += 1


def do_some_selection_sortin():
    L = [5, 1, 9, 8, 3, 4, 6, 5]

    selection_sort(L)


def merge(left, right, compare):
    """Assumes left and right are sorted lists and compare
    defines an ordering on the elements.

    Returns a new sorted (by compare) list containing the same elements
    as (left + right) would contain."""

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(L, compare = lambda x, y: x < y):
    """Assumes L is a list, compare defines an ordering
    of elements on L.

    Returns a new sorted list with the same elements as L."""

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[0:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def do_some_merge_sortin():
    L = [2, 1, 4, 5, 3]

    print(merge_sort(L), merge_sort(L, lambda x, y: x > y))


class IntDict(object):
    """A dictionary with integer keys."""

    def __init__(self, num_buckets):
        """Create an empty dictionary."""

        self.buckets = []
        self.num_buckets = num_buckets

        for i in range(num_buckets):
            self.buckets.append([])

    def add_entry(self, key, dict_val):
        """Assumes key an int. Adds an entry."""

        hash_bucket = self.buckets[key % self.num_buckets]

        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
            
        hash_bucket.append((key, dict_val))

    def get_value(self, key):
        """Assumes key is an int.

        Returns value associated with key."""

        hash_bucket = self.buckets[key % self.num_buckets]

        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        
        return None

    def __str__(self):
        result = '{'

        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ': ' + str(e[1]) + ','

        # result[:-1] omits the last comma
        return result[:-1] + '}'


if __name__ == '__main__':
    # do_some_binary_searchin()

    # do_some_selection_sortin()

    # do_some_merge_sortin()

    D = IntDict(17)

    int_list = range(10 ** 5)

    for i in range(20):
        key = random.choice(int_list)
        D.add_entry(key, i)

    print('The value of the IntDict is:')
    print(D)
    print('\n', 'The buckets are:')

    for hash_bucket in D.buckets:
        print(hash_bucket)

