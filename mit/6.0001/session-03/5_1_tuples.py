t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)

t3 = (1,)
print(t3)

t4 = (1)
print(t4)

print(3 * ('a', 2))

t5 = (1, 'two', 3)
t6 = (t5, 3.25)
print(t6)

print((t5 + t6))
print((t5 + t6)[3])
print((t5 + t6)[2:5])

def intersect(t1, t2):
    """
    Assumes t1 and t2 are tuples
    Returns a tuple containing elements that are in
    both t1 and t2
    """
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

t7 = ('a', 'b', 'c', 'd', 'e')
t8 = ('c', 'd', 'b', 'f', 'g', 'h')

print(intersect(t7, t8))
        
x, y = (3, 4)
print(x)
print(y)

a, b, c = 'xyz'
print(a, b, c)

def findExtremeDivisors(n1, n2):
    """
    Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and
        the largest common divisor of n1 and n2. If no common divisor,
        returns (None, None)
    """
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

low, high = findExtremeDivisors(100, 200)

print(low)
print(high)
