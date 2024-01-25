# Create a dictionary
#mydict = {
#            "name": "Max",
#            "Age": 17,
#            "city": "New York"
#          }
#print(mydict)

# add something to the dictionary
#mydict["email"] = "bryanherrera@gmail.com"
#print(mydict)

# delete an specific item from the dictionary
#mydict.pop("Age")
#print(mydict)

# check if a key is in the dict
# Way num 1
#if "name" in mydict:
#    print(mydict["name"])

# Way num 2
#try:
#    print(mydict["name"])
#except:
#    print("Error")


# Loop through a dictionary
#for key, value in mydict.items():
#    print(key, value)

# merge two dictionaries
my_dict = {
            "name": "Max",
            "age": 17,
            "email": "max@gmail.com"
          }

mydict_2 = dict(name="marry", age=27, city="Boston")

my_dict.update(mydict_2)
print(my_dict)