# nested
a = ["a", "b"]
nested_list = [1, 2, a]
print(nested_list)

ints = range(0, 10)
print(len(ints))

# + and * work on lists
list1 = [1, 2, 3]
list2 = [4, 5]
print(list1 + list2)
print(list2 * 3)

# indices
neg = ints[-3]
print(neg)

# slice
print(ints[7:])
print(ints[7:9])
print(ints[7:10])
print(ints[-3:])

# step
# evens
print(ints[0::2])

# odds
print(ints[1::2])

# reverse
print(ints[::-1])

# mutable
list3 = [1, 2, 3, 4]
list4 = list3
list3[3] = 5
print(list3)
print(list4)

# test for key
list5 = [1, 2, 3, 4]
print(5 in list5)

# append
list6 = ['a', 'b', 'c']
list6.append('d')
print(list6)

# output?
list7 = [0, 1, [2]]

list7[2][0] = 3
print list7
#=> [0, 1, [3]]

list7[2].append(4)
print list7
#=> [0, 1, [3, 4]]

list7[2] = 2
print list7
#=> [0, 1, 2]

print 'a' in list6
