#import it
from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]

# Get all the possible combinations of a
comb = combinations(a, 2)
print(list(comb))

# get all possible combinations of a but with replacements
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))