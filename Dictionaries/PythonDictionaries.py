thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

'''
DICTIONARY:
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is collection which is ordered, changeable and do not
  allow duplicates
- Dictionaries are written with curly backets, and have keys and values
'''
# example: (create and print a dictionary)
anotherdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(anotherdict)

'''
DICTIONARY ITEMS:
- Dictionary items are ORDERED, CHANGEABLE, and do NOT allow duplicates
- Dictionary items are presented in key:value pairs, and can be referred
  to by using the key name
'''
# example: (print the "brand" value of the dictionary)
exampledict = {
    "brand" : "Mustang",
    "model" : "Mustang",
    "year" : 1964
}
print(exampledict["brand"])

'''
ORDERED OR UNORDERED:
- When we say that dictionaries are ordered, it means that the items
  have a defined order, and that order will not change
- Unordered means that the items do not have a defined order,
  you cannot refer to the item by using an index

CHANGEABLE:
- Dictionaries are changeable, meaning that we can change, add or
  remove items after the dictionary has been created
  
DUPLICATES NOT ALLOWED:
- Dictionaries cannot have two items with the same key
'''
# example: (duplicate values will overwrite exisitng values)
adict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2025
}
print(adict)
    # the second year will overwrite the first year

'''
DICTIONARY LENGTH:
- To determine how many items a dictionary has, use the len() function
    - the same as all the others
'''
# example: (print the number of items in the dictionary)
print(len(thisdict))

'''
DICTIONARY ITEMS - DATA TYPES:
- The values in dictionary items can be that of any data type
'''
# example: (String, int, boolean, and list data types)
bdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964,
    "color" : ["red", "white", "blue"]
}
'''
type()
- from python's perspective, dictionaries are defined as objects with
  the data type 'dict':
<class 'dict'>
'''
# example: (print the data type of a dictionary)
cdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(type(cdict))

'''
THE DICT() CONSTRUCTOR:
- It is also possible to use the dict() constructor to make a dictionary
'''
# example: (using the dict() method to make a dictionary)
ddict = dict(name = "John", age = 36, country = "Norway")
print(ddict)


'''
PYTHON COLLECTIONS (ARRAYS)
There are four collection data types in the python programming language:
- LIST: is a collection which is ordered and changeable, allowing
  for duplicate members
- TUPLE: is a collection which is ordered, unchangeable allowing
  duplicate members
- SET: is a collection which is unordered, unchangeable, unindexed,
  not allowing for duplicate members


- when choosing a collection type, it is useful to understand
the properties of that type. Choosing the right type for particular
data set could mean retention of meaning, and, it could
mean an increase in efficiency or security.
'''

# EXERCISE: which one of these is a dictionary?
# x = ('apple', 'banana', 'cherry')
# x = {'type' : 'fruit', 'name' : 'banana'}   # correct
# x = ['apple', 'banana', 'cherry']