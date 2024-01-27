# Generator
def mygenerator():
    yield 1
    yield 2
    yield 3

#yield object
g = mygenerator()

# sum them 
print(sum(g))