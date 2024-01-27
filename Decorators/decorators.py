
# Creates a decorator function saying the start and the end
def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

# function to print the name
# decorator included to show the start and end message when printing the name alex
@start_end_decorator
def print_name():
    print('alex')

# This makes the decorator work
#print_name = start_end_decorator(print_name)

print_name()