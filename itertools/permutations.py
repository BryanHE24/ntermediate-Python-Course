#import it
from itertools import permutations

a = [1,2,3]

# Get all the possible orderings  of a 
perm = permutations(a, 2)
print(list(perm))