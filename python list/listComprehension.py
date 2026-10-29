fruits = ['banana', 'cherry', 'pineapple', 'watermelon']

newList = [x if x != 'banana' else 'orange' for x in fruits]

print(newList)