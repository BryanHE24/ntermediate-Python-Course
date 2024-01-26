#*****************************************************************************
# Errors
#a = 5
#b =c
 

#F = open('somefile.txt')

#a = [1,2,3]
#a.remove(4)
#print(a)


#mydict = {'name':'max'}
#mydict['age']
#********************************************************************************

# raise an exception because of a condition
#x = -5
#if x < 0:
    #raise Exception('x should be positive')

#
#x = -5
#assert(x>=0), 'x is not positive'

# Handle exceptions
#try:
#    a = 5 / 0
#except TypeError as e:
#    print(e)


#try:
#    a = 5 / 0
#    b = a + 4
#except ZeroDivisionError as e:
#    print(e)
#except TypeError as e:
#    print(e)
#else:
#    print('Everything is fine')
#finally:
#    print('Finished')

# define my own exceptions
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value too high')
try:
    test_value(200)

except ValueTooHighError as e:
    print(e)