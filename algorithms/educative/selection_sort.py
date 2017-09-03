def swap(array, i, j):
    """
    Swaps two values in an array. Mutates the original array.
    """
    array[j], array[i] = array[i], array[j]
    return

def indexOfMinimum(array, startIndex):
    """
    Returns the index of the smallest value that occurs with
    index of startIndex or greater.
    """

    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(startIndex + 1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minIndex = i

    return minIndex

def selectionSort(array):
    """
    Loop over each position in the array.
    For each position, find the index of the minimum value
        in the subarray starting at that position.
    Swap the value at the position and at the minimum index.
    """

    for i in range(len(array)):
        minIndex = indexOfMinimum(array, i)
        swap(array, i, minIndex)

    return

if __name__ == '__main__':
    a = [1, 3, 2, 4]
    swap(a, 1, 2)
    print(a)

    b = [5, 3, 4, 2, 1]
    print(indexOfMinimum(b, 2))

    c = [1, 4, 3, 2, 5]
    print(indexOfMinimum(c, 1))

    selectionSort(b)
    selectionSort(c)
    print(b)
    print(c)

