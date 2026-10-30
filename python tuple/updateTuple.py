fruits = ('apple', 'banana', 'cherry', 'watermelon')

x = list(fruits)

x.append('guava')

fruits = tuple(x)

print(fruits)

x = list(fruits)

x.remove('banana')

fruits = tuple(x)

print(fruits)