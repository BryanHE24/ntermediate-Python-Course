# List
a = [1, 2, 3, 4, 5, 6]
# filter the list by only the even numbers
filter_a = filter(lambda x: x%2==0, a)
# print it
print(list(filter_a))

# the same using list
c = [x for x in a if x%2==0]
print(c)