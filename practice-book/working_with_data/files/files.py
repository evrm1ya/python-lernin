txt = open('foo.txt').read()
print txt

txt2 = open('foo.txt').readlines()
print txt2

txt3 = open('foo.txt')
print txt3.readline()
print txt3.readline()
print txt3.readline()
print txt3.readline()
print txt3.readline()

# writing
txt4 = open('bar.txt', 'w')
txt4.write('a\nb\nc')
txt4.close()

# appending
txt5 = open('bar.txt', 'a')
txt5.write('\nd\ne\nf')
txt5.close()

# writelines convenient when data is
# available as a  list of lines
txt6 = open('bar.txt', 'a')
txt6.writelines(['\na\n', 'b\n', 'c\n'])
txt6.close()
