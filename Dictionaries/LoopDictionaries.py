'''
LOOPING THROUGH A DICTIONARY:
- You can loop through a dictionary by using a for loop
- When looping through a dictionary, the return value are the KEYS
  of the dictionary, but there are methods to return the values as well
'''
# example: (print all KEY names in the dictionary one by one)
thisdict = {
    "brand" : "porsche",
    "model": "911",
    "year":2024
}
for x in thisdict:
    print(x)
    # this will print: (brand
    #                   model
    #                   year)

# example: (print all VALUES in the dictionary one by one)
for x in thisdict:
    print(thisdict[x])
        # you access the different values from the dictionary
        # without doing anything you would just print the keys
        # as you could see before
    # this will print: 
        # porsche
        # 911
        # 2024

# example: (You can also use the values() method to return the values
#           of a dictionary)
for x in thisdict.values():
    print(x)
    # this will print the same thing as the example above


# example: (you can use the keys() method to return the keys of a 
#           dictionary)
for x in thisdict.keys():
    print(x)
    # this will print:
        # brand
        # model
        # year
    
# example: (loop through both keys and values, by using the items()
#           method)
for x, y in thisdict.items():
    print(x,y)
    # this will now print:
    # brand porsche
    # model 911
    # year 2024


# EXAMPLE: what is a correct syntax for looping trhough the values
#           of this dictionary?
#       x = {'type' : 'fruit', 'name' : 'apple'}
# 1.) for y in x.values():
#       print(y)  # correct
# 2.) for y in x:
#       print(y)
# 3.) for y in x:
#       print(y.value())