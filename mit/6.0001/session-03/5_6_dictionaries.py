month_numbers = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May'
}

print('The third month is ' + month_numbers[3])
dist = month_numbers['Apr'] - month_numbers['Jan']
print('Apr and Jan are', dist, 'months apart')

keys = []

for e in month_numbers:
    keys.append(str(e))

print(keys)
keys.sort()
print(keys)

birth_stones = {
    'Jan': 'Garnet',
    'Feb': 'Amethyst',
    'Mar': 'Acquamarine',
    'Apr': 'Diamond',
    'May': 'Emerald'
}

# view object example
# changes with the object it is associated with
months = birth_stones.keys()
print(months)
birth_stones['June'] = 'Pearl'
print(months)
