import sys
# function that will print a list of numbers from 0-10
def firstn(n):
    # set an empty list
    nums = []
    # set num to cero
    num = 0
    # increase from cero to n
    while num < n:
        nums.append(num)
        num += 1
    # return the list with the values
    return nums
# print and set the value for n and sum firstn
print(sys.getsizeof((firstn(1000000))))


# generator that will print a list of numbers from cero to ten but it doesnt need to store the data in a list.
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(sys.getsizeof((firstn_generator(1000000))))
