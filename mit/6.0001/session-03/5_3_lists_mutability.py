techs = ['MIT', 'Caltech']
ivys = ['Harvard', 'Yale', 'Brown']
univs = [techs, ivys]
univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print('univs =', univs)
print('univs1 =', univs1)
print(univs == univs1)

print(id(univs) == id(univs1))
print('Id of univs =', id(univs))
print('Id of univs1 =', id(univs1))

print('Ids of univs[0] and univs[1]', id(univs[0]), id(univs[1]))
print('Ids of univs1[0] and univs1[1]', id(univs1[0]), id(univs1[1]))

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 + l2
print('l3 =', l3)

l1.extend(l2)
print('l1 =', l1)

l1.append(l2)
print('l1 =', l1)
