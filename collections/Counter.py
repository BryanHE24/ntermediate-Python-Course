# Counter collection
from collections import Counter

# Count how many a's, b's and c's and the most common
a = "aaaaaaaaabbbbccccc"
my_counter = Counter(a)
print(my_counter.most_common(1)[0][0])