# Write a function `isIn` that accepts
# two strings as arguments and returns
# True if either string occurs anywhere
# in the other, and False otherwise.

def is_in(a, b):
    if a in b or b in a:
        return True
    return False

print(is_in('test', 'testing'))
print(is_in('testing', 'test'))
print(is_in('test', 'fail'))

# 4.1.2 Keyword Arguments and Default Values

def print_name(first_name, last_name, reverse):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

print_name('Olga', 'Puchmajerova', False)
print_name('Olga', 'Puchmajerova', reverse = False)
print_name('Olga', last_name = 'Puchmajerova', reverse = False)
print_name(last_name = 'Puchmajerova', first_name = 'Olga', reverse = False)

def print_name_two(first_name, last_name, reverse = False):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

print_name_two('Olga', 'P')
print_name_two('Olga', 'P', True)
print_name_two('Olga', 'P', reverse = True)

# 4.1.3 Scoping

# def f(x):
#     y = 1
#     x = x + y
#     print('x = ', x)
#     return x
# 
# x = 3
# y = 2
# z = f(x)
# print('z =', z)
# print('x =', x)
# print('y =', y)

# Nested scopes

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z =', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x =', x)
    return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()

