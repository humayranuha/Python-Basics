thisSet = {'apple', 'banana', 'cherry', 'pineapple', 'watermelon', 'guava'}
thisSet.remove('guava')
print(thisSet)
thisSet.discard('watermelon')
print(thisSet)

x = thisSet.pop()
print(x)

thisSet.clear()
print(thisSet)

del thisSet