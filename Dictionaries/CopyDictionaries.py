'''
COPY A DICTIONARY:
- You cannot copy a dictionary simply by typing dict2 = dict1, because
  dict2 will only be a reference to dict1
  changes made in dict1 will automatically also be made in dict2
- there are ways to make a copy, one way is to use the built-in
  dictionary method copy()
'''
# example: (make a copy of a dictionary with the copy() method)
thisdict = {
    "brand" : "porsche",
    "model" : 911,
    "year" : 2024
}
mydict = thisdict.copy()
    # the .copy() is a method
print(mydict)
    # this will print: {'brand' : 'porsche', 'model':922, 'year':2024}
    # now this will have two distinct dictionaries, not just references
    # and they will contain the same keys and items
    
    
# another way to make a copy is to use the built-in function dict()
# example: (make a copy of a dictionary with the dict() function)
thisdict2 = {
    "brand":"porsche",
    "model":911,
    "year":2024
} 
mydict2 = dict(thisdict2)
    # the dict() is a function
print(mydict2)
    # this will now print:
    # {'brand': 'porsche', 'model': 911, 'year': 2024}

# EXERCISE: what is a correct syntax for making a copy of this dictionary
#      x = {'type':'fruit', 'name':'apple'}
# 1.) y = x.clone() 
# 2.) y = x.duplicate()
# 3.) y = x.copy()  # correct