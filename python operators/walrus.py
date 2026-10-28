# Python 3.8 introduced the := operator, known as the "walrus operator". 
# It assigns values to variables as part of a larger expression:

x = ['apple', 'banana']

if (count := len(x)) > 1:
    print(f"List has {count} elements")