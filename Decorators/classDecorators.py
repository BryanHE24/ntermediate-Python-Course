# keep track of how many times i have executed num.calls

# This decorator will count the number of times that it's executed starting from cero
class CountCalls:
    def __init__(self,func):
        self.func = func
        self._num_calls = 0

    # This will update the numbers of times that it has been executed
        def __call__(self, *args, **kwargs):
            self._num_calls += 1
            print('This is executed {self.num_calls} times')
            return self.func(*args, **kwargs)
#        

# This function has a Decorator for count how many times the "hello" is executed
@CountCalls
def say_hello():
    print("Hello")

# execute the function say hello
say_hello()
say_hello()