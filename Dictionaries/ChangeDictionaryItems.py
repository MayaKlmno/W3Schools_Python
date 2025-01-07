'''
CHANGE VALUES:
- You can change the value of a specified item by referring to its key
  name:
'''
# example: (change the "year" to 2018)
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["year"] = 2018

'''
UPDATE DICTIONARY:
- The update() method will update the dictionary with the items from 
  the given argument
- The argument must be a dictionary, or an iterable object with key:value
  pairs
'''
# example: (update the "year" of the car by using the update() method)
thisdict2 = {
    "brand":"Ford",
    "model":"mustang",
    "year" :1964
}
thisdict2.update({"year":2025})
    # now the value of the year in the dictionary is 2025 instead
    # of 1964

# EXERCISE: conisder the following code
#       x = {'type' : 'fruit', 'name':'banana'}
#       what is a correct syntax for chaning the type from fruit
#       to berry
# 1.) x{'type'} = 'berry'
# 2.) x['type'] = 'berry'   # correct
# 3.) x.get('type') = 'berry'