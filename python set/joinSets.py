set1 = {'apple', 'banana', 'cherry'}
set2 = {'samsung', 'microsoft', 'apple'}

set3 = set1.union(set2) # set1 | set2
print(set3)

set4 = set1.intersection(set2) # set1 & set2
print(set4)

set5 = set1.difference(set2) # set1 - set2
print(set5)

set6 = set1.symmetric_difference(set2) # set1 ^ set2
print(set6)