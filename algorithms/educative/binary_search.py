phonetic = [
    'alpha', 'bravo', 'charlie', 'delta',
    'echo', 'foxtrot', 'golf', 'hotel',
    'india', 'juliett', 'kilo', 'lima',
    'mike', 'november', 'oscar', 'papa',
    'quebec', 'romeo', 'sierra', 'tango',
    'uniform', 'victor', 'whiskey', 'xray',
    'yankee', 'zulu'
]

def print_result(index, result, num_guesses):
    print({ 
        'index': index,
        'result': result, 
        'num_guesses': num_guesses 
    })

# for educative
def doSearch(array, targetValue):
    """
    Returns the index of the targetValue in the array or -1 if
    targetValue not found in array.
    """

    minimum = 0
    maximum = len(array) - 1

    while maximum >= minimum:
        guess = (maximum + minimum) // 2

        if array[guess] == targetValue:
            return guess 
        elif array[guess] < targetValue:
            minimum = guess + 1
        else:
            maximum = guess - 1

    return -1


def do_search(array, target):
    minimum = 0
    maximum = len(array) - 1
    num_guesses = 0

    while maximum >= minimum:
        num_guesses += 1
        guess = (maximum + minimum) // 2

        if array[guess] == target:
            print_result(guess, array[guess], num_guesses)
            return guess

        if array[guess] < target:
            minimum = guess + 1
        else:
            maximum = guess - 1

    print_result(-1, None, num_guesses)
    return -1

if __name__ == '__main__':
    print('sierra')
    do_search(phonetic, 'sierra')

    print('bravo')
    do_search(phonetic, 'bravo')

    print('dog')
    do_search(phonetic, 'dog')

    print('zulu')
    do_search(phonetic, 'zulu')

    print('alpha')
    do_search(phonetic, 'alpha')

    print('mike')
    do_search(phonetic, 'mike')
