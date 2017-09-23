# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def insert_char_into_seq(char, l):
    length = len(l[0]) + 1
    inserted = []

    for seq in l:
        for i in range(length):
            if i == 0:
                inserted.append(char + seq)
                continue
            inserted.append(seq[:i] + char + seq[i:])

    return inserted

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    length = len(sequence)

    if length == 1:
        return [sequence]

    return insert_char_into_seq(sequence[0], get_permutations(sequence[1:]))




def test_get_permutations(sequence, expected):
    result = get_permutations(sequence)
    print('Input:', sequence)
    print('Expected Output:', expected)
    print('Actual Output:', result)
    print('Pass:', result == expected)

if __name__ == '__main__':
    import timeit

    print(insert_char_into_seq('p', ['le', 'el']))
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    test_get_permutations(
        'cow',
        ['cow', 'ocw', 'owc', 'cwo', 'wco', 'woc']
    )

    print(timeit.timeit("get_permutations('rust')",
        setup="from __main__ import get_permutations",
        number=100
    ))

    print(timeit.timeit("get_permutations('super')",
        setup="from __main__ import get_permutations",
        number=100
    ))

    print(timeit.timeit("get_permutations('supercal')",
        setup="from __main__ import get_permutations",
        number=100
    ))

    print(timeit.timeit("get_permutations('supercali')",
        setup="from __main__ import get_permutations",
        number=100
    ))
