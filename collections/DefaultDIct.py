# default dict 
from collections import defaultdict
# create a default dict and if there's no default value use an empty list
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['a'])