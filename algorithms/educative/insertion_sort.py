
def insert(array, rightIndex, value):
    while rightIndex > -1:
        if value > array[rightIndex]:
            break

        array[rightIndex + 1] = array[rightIndex]
        rightIndex -= 1

    array[rightIndex + 1] = value

    return

def insertionSort(array):
    for i in range(1, len(array)):
        insert(array, i - 1, array[i])
        

if __name__ == '__main__':
    a = [3, 5, 7, 11, 13, 2, 9, 6]
    insert(a, 4, 2)
    print(a)

    insert(a, 5, 9)
    print(a)

    insert(a, 6, 6)
    print(a)

    b = [1, 2, 0]
    insert(b, 1, 0)
    print(b)

    c = [3, 5, 7, 11, 13, 2, 9, 6]
    insertionSort(c)
    print(c)

