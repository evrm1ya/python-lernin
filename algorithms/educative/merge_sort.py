# Takes in an array that has two sorted subarrays,
# from [p..q] and [q+1..r], and merges the array
def merge(array, p, q, r):
    lh = q - p + 1
    rh = r - q

    L = [0] * (lh)
    R = [0] * (rh)

    for i in range(0, lh):
        L[i] = array[p + i]

    for j in range(0, rh):
        R[j] = array[q + 1 + j]
    
    i, j, k = 0, 0, p

    while i < lh and j < rh:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < lh:
        array[k] = L[i]
        i += 1
        k += 1

    while j < rh:
        array[k] = R[j]
        j += 1
        k += 1


def mergeSort(array, p, r):
    if len(array) == 0:
        return array

    if p < r:
        m = (p + r) // 2
        mergeSort(array, p, m)
        mergeSort(array, m + 1, r)
        merge(array, p, m, r)


if __name__ == '__main__':
    l1 = [1, 3, 5, 2, 4, 6]
    merge(l1, 0, 2, 5)
    print(l1)

    l2 = [1, 3, 5, 2, 4, 6, 7]
    merge(l2, 0, 2, 6)
    print(l2)

    l3 = [1]
    mergeSort(l3, 0, 0)
    print(l3)

    l4 = []
    mergeSort(l4, 0, 0)
    print(l4)

    l5 = [4, 2, 1, 3]
    mergeSort(l5, 0, 3)
    print(l5)

    l6 = [4, 3, 2, 1, 0, -1, -99]
    mergeSort(l6, 0, 6)
    print(l6)
    
