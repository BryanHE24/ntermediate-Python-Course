# counter generator 
def countdown(num):
    # this will print 'starting' at the first run
    print('Starting')
    # then it will run until it reaches the first yield and will return the number
    while num >=0:
        yield num 
        num += 1
        


cd = countdown(1)

# First Try
value = next(cd)
print(value)

# second Try
value = next(cd)
print(value)

# third Try
value = next(cd)
print(value)
# third Try
value = next(cd)
print(value)

print('ended')
