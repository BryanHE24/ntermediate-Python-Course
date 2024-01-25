# import
from itertools import groupby

###########################################################################
#a = [1,2,3,4]

# Example 1
# This functionis to valid if the value is smaller than 3
#def smaller_than_3(x):
    #return x > 3

# group it using the key
#group_obj = groupby(a, key=smaller_than_3)

# iterate over the object
#for key, value in group_obj:
    #print(key, list(value))
#############################################################################

# Example 2
# Dictionary of persons
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'claire', 'age': 28 }]

# Group persons by the same age and print it 
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

