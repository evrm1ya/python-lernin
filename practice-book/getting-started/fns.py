# How many multiplications are performed
# when each of the following are executed?

def square(x):
    return x * x

print square(5)
#=> 1
print square(2 * 5)
#=> 2

# what is the output

x = 1
def f():
    return x

print x
# => 1
print f()
# => 1

y = 1

def g():
    y = 2
    return y

print y
#=> 1
print g()
#=> 2
print y
#=> 1
# must use global modifier to modify global var

#a = 1
#
#def h():
#    b = a
#    a = 2
#    return a + b
#
#print a
##=> 1
#print h()
##=> 3
##=> error
#print a
##=> 1

p = 2

def l(q):
    p = q * q
    return p

r = l(3)

print p, r
#=> 2 9

def increment(num, step = 1):
    return num + step

print(increment(2))

def my_add(step = 1):
    def fn(num):
        return num + step
    return fn

add1 = my_add()
add2 = my_add(2)

print(add1(3))
print(add2(6))

# lambdas

def fxy(f, x, y):
    return f(x) + f(y)

cube = lambda x: x ** 3

print(cube(2))
print(fxy(cube, 2, 3))

list1 = range(1, 6)

mapped = [cube(x) for x in list1]
print(mapped)

mapped2 = map(cube, list1)
print(mapped2)

filteredMapped = [cube(x) for x in list1 if x % 2 == 0]
print(filteredMapped)

isEven = lambda x: x % 2 == 0

filteredMapped2 = map(cube, filter(isEven, list1))
print(filteredMapped2)

# Write a function istrcmp to compare two strings, ignoring the case
def istrcmp(x, y):
    return x.lower() == y.lower()

print(istrcmp('python', 'Python'))
print(istrcmp('LaTex', 'Latex'))
print(istrcmp('a', 'b'))
