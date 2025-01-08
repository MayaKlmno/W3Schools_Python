'''
REMOVING ITEMS:
- There are several methods to remove items from a dictionary
'''
# example: (the opo() methods to remove the item with the specified
#           items from a dictionary)
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.pop("model")
print(thisdict)
    # now it won't print the model since you poped/removed it

# example: (the popitem() method removes the last inserted item)
exampledict = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : 1964
}
exampledict.popitem()
print(exampledict)
    # now the year won't be there anymore since it was the last method

# example: (the del keyword removes the item with the specified 
#           key name)
exampledict2 = {
    "brand" : "Ford", 
    "model" : "Mustang",
    "year" : 1964
}
del exampledict2["model"]
print(exampledict2)
    # this will now only have the brand and the year
    
'''
BAD EXAMPLE: (the del keyword can also delete the dictionary completely)
thisidct= {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : 1964
}
del thisdict
print(thisdict)
    # this will cause an error because "thisdict" no longer exists
    # and you cannot print something that doesn't exist
'''

# example: (The cear() method empties the dictionary)
exampledict3 = {
    "brand" : "Ford", 
    "model" : "Mustang",
    "year" : 1964
}
exampledict3.clear()
print(exampledict3)
    # this will now be an empty dictionary

# EXERCISE: what is a dictionary method for removing an item from a 
#           dictionary
# delete()
# remove()
# pop()  # correct