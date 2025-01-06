'''
ACCESING ITEMS:
- You can access the items of a dictionary by referring to its key
  name, inside square brackets:
'''
# example: (get the value of the "model" key)
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict["model"]
    # the keys are on the left, and what the keys hold is on the right

# there is also a method called get() that will give you the same result:
# example: (get the value of the "model" key)
x = thisdict.get("model")

'''
GET KEYS:
- the keys() method will return a list of all the keys in the dictionary
'''
# example: (get a list of the keys)
x = thisdict.keys()

# the list of the keys is a view of the dictionary, meaning that any
    # changes done to the dictionary will be reflected in the keys list
# example: ()