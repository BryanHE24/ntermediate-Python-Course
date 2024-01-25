from functools import reduce
#list
a = [1,2,3,4]

# compute the product of all the elements of a
product_a = reduce(lambda x,y: x*y, a)
print(product_a)