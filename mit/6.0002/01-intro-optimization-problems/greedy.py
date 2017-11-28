class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                + ', ' + str(self.weight) + '>'
        return result


def value(item):
    return item.get_value()


def weight_inverse(item):
    return 1.0 / item.get_weight()


def density(item):
    return item.get_value() / item.get_weight()


def greedy(items, max_weight, key_function):
    """Assumes Items a list, max_weight >= 0,
    key_function maps elements of Items to numbers."""

    items_copy = sorted(items, key = key_function, reverse = True)

    result = []

    total_value, total_weight = 0.0, 0.0

    for i, item in enumerate(items_copy):
        weight = item.get_weight()

        if (total_weight + weight) <= max_weight:
            result.append(item)
            total_weight += weight
            total_value += item.get_value()

    return (result, total_value)


def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []

    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))

    return items


def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)

    print('Total value of items taken is', val)
    
    for item in taken:
        print('   ', item)


def test_greedys(max_weight = 20):
    items = build_items()

    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)

    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)

    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)

    print()


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


def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = None
    
    for items in pset:
        items_val = 0.0
        items_weight = 0.0

        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)

        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items

    return (best_set, best_val)


def test_best(max_weight = 20):
    items = build_items()
    pset = gen_powerset(items)
    taken, val = choose_best(
        pset,
        max_weight,
        Item.get_value,
        Item.get_weight
    )

    print('Total value of items taken is', val)

    for item in taken:
        print(item)


if __name__ == '__main__':
    test_greedys()
    test_greedys(10)

    test_best()
