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
# example: (Add a new item to the origional dictionary, and see that the 
#           keys list gets updated as well)
car = {
    "brand" : "Ford",
    "model" : "mustang",
    "year" : 1964
}
y = car.keys()
print(y) # this is before the change to the dictonary
car["color"] = "white" # changing the key for color
print(y) # now the key set will change as well

'''
GET VALUES:
- The values() method will return a list of all the values in the 
  dictionary
'''
# example: (get a list of the values)
z = thisdict.values()

# the list of the values is a VIEW of the dictionary, meaning that any 
#   changes done to the dictionary will be reflected in the values 
#   list
# example: (make a change in the origional dictionary, and see the
#           values list gets updated as well)
car2 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
a = car2.values()
print("value of a before: ")
print(a)
car2["year"] = 2025
print("this is a after you change the origional: ")
print(a)
    # these are the values NOT the keys

# example: (add a new item to the origional dictionary, and see
#           that the values list gets updated as well)
car3 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
b = car3.values()
print(b) # this is b beofre the change
car3["color"] = "red" # we change the value
print(b) # this is the value of be after the change
    # now there is a new key and value for the color

'''
GET ITEMS:
- The items() method will return each item in a dictionary, as tuples
  in a list
'''
# example: (get a list of the key:value pairs)
w =thisdict.items()
print(w)
    # this will print: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# the returned list is a view of the items in the dictionary, meaning
#   that any changes done to the dictionary will be reflected in the items
#   list.
# example: (make a change in the origional dictionary, and see that the
#           items list gets updated as well)
car4 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
c = car4.items()
print(c)   # before the change
car4["year"] = 2025
print(c)  # after the change

# example: (add a new item to the origional dictionary, and see that the 
#           items list gets updated as well)
car5 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
d = car5.items()
print(d)   # before the change
car5["color"] = "red"
print(d)    # after the change

'''
CHECK IF THE KEY EXISTS:
- To determine if a specified key is present in a dictionary use the 
  in keyword
'''
# example: (check if "model" is present in the dictionary)
thisdict2 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
if "model" in thisdict2:
    print("Yes, 'model' is one of the keys in the thisdict2 dictionary")

# EXERCISE: True or False, You can access item values by referring to 
#           the key name
#           True