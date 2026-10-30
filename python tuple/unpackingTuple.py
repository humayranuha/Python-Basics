fruits = ('apple', 'banana', 'cherry')
colors = ('green', 'yellow', 'red')
numbers = (1, 2, 3, 4, 5)

(x, y, z) = fruits
(p, *q) = colors
(a, *b, c) = numbers

print(x, y, z, p, q, a, b, c)