# Generator
def mygenerator():
    yield 1
    yield 2
    yield 3

#yield object
g = mygenerator()

# show one item per run
# first try
value = next(g)
print(value)

# second try
value = next(g)
print(value)

# third try
value = next(g)
print(value)