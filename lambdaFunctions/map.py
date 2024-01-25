# Lambda function using map to multiply the elements of a Two times and print it as a list
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# the same but different method
c = [x*2 for x in a]
print(c)