# Generator
def mygenerator():
    yield 1
    yield 3
    yield 2

#yield object
g = mygenerator()

# sort them
print(sorted(g))