# create a set
#myset = {1, 2, 3}
#print(myset)

# way 2
#myset = set([1,2,3])

# Empty set
myset = set()

# add something to a set
myset.add(1)
myset.add(2)
myset.add(3)

# remove elements 
#myset.remove(3)
#myset.clear()

# iterate over a set
#for x in myset:
#    print(x)

# check if something is in the set
#if 1 in myset:
#    print("yes")

# put together two sets,
#odds = {1,3,5,7,9}
#evens = {0,2,4,6,8}
#primes = {2,3,5,7}

#u = odds.union(evens)
#print(evens)

# calculate the interception of two sets
#i = odds.intersection(primes)
#print(i)

# diference between sets
#setA = {1,2,3,4,5,6,7,8,9}
#setB = {1,2,3,10,11,12}

#diff = setA.difference(setB)
#print(diff)

# is setA a subset of setB?
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

print(setA.issubset(setB))