'''
ADDITNG ITEMS:
- Adding an item to the dictionary is done by using a new index key and 
  assigning a value to it. 
'''
# example:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)


'''
UPDATE DICTIONARY:
- The update() method will update the dictionary with the items from
  a given argument. 
- If the item doesn't exist, the item will be added.
- The argument must be a dictionary, or an iterable object with
  key:value pairs
'''
# example: (add a color item to the dictionary by using the update()
#           method)
thisdict2 = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict2.update({"color":"red"})

# EXERCISE: which one of these dictionary methods can be used to add
#            items to a dictionary
# add()
# insert()
# update()    # correct