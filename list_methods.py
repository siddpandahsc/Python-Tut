list1 = [3, 6, 1, 2, 8, 4, 5, 9, 0]
list2 = ['banana', 'apple', 'mango', 'orange']
list3 = list1 + list2
# list1.extend(list2)
print(list3)
print(list1)
# list2.append('cherry')
print(list2)
# list2.insert(1, 'swahili')
print(list2)
# list2.remove('banana')
print(list2)
# list2.clear()
print(list2)
print(list2.index('mango'))
list1.sort()
print(list1)
list2.reverse()
print(list2)
list3 = list2.copy()
print(list3)
# list2.pop()
print(list2)
# list2.pop(1)
del list2[0]
print(list2)
del list2
print(list2)