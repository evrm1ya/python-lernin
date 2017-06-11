# Write a program that takes three vars - x, y, z
# Print the largest odd number
# If none are odd, print it
all_even = [2, 4, 6]
one_odd = [5, 2, 0]
all_odd = [11, 7, 5]

def get_odds(numbers):
    return [x for x in numbers if x % 2 != 0]

def new_max(numbers):
    result = 0
    for x in numbers:
        if x > result:
            result = x
    return result

def largest_odd_number(x, y, z):
    odds = get_odds([x, y, z])
    if len(odds) == 0:
        return 'None of the numbers are odd'
    return new_max(odds)

print(get_odds(all_even))
print(get_odds(all_odd))
print(get_odds(one_odd))
print(largest_odd_number(2, 4, 6))
print(largest_odd_number(5, 2, 0))
print(largest_odd_number(11, 7, 5))
print(largest_odd_number(5, 7, 11))

# print x based on input
# numXs = int(input('How many times should I print the letter x? '))
# toPrint = ''
# 
# while numXs > 0:
#     toPrint = toPrint + 'x'
#     numXs = numXs - 1
# 
# print(toPrint)

# Find a positive integer that is 
# divisible by both 11 and 12
x = 1

while True:
    if x % 11 == 0 and x % 12 == 0:
        break
    x = x + 1

print(x, 'is divisible by 11 and 12')

# Write a program that asks the user to input
# 10 integers, and then prints the largest odd
# number that was entered

highest = 0

for i in range(0, 10):
    number = int(input('Enter an integer: '))
    if number % 2 == 0:
        continue
    if number > highest:
        highest = number

if highest == 0:
    print('No odd or nonzero integers were entered')

print('Highest odd number: %d ' % highest)



