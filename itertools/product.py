# Import product
from itertools import product

# create a product iterator
a = [1,2]
b = [3,4]

# product of a and b (Also can add the repeat=<number> method to repeat)
prod = product(a,b,) #repeat=2)
print(list(prod))