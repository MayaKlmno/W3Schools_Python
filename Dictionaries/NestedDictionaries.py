'''
NESTED DICTIONARIES:
- a dictionary can contain dictionaires, this is called nested dictionaries
  ( a dictionary in a dictionary)
'''
# example: (create a dictionary that contains three dictionaries)
myfamily = {
    "child1" : {
        "name" : "Aaron",
        "year" :2004
    },
    "child2" : {
        "name" : "Dean",
        "year" : 2007
    },
    "child3" : {
        "name" : "Jameson",
        "year" : 2008
    }
}

# or if you want to add three dictionaries into a new dictionary
# example: (create three dictionaries, then create one dictionary
#           that will contain the other three dictionaries)
child1 = {
    "name" : "Aaron",
    "year" : 2004
}
child2 = {
    "name" : "Dean",
    "year" : 2007
}
child3 = {
    "name" : "Jameson",
    "year" : 2008
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

'''
ACCESS ITEMS IN NESTED DICTIONARIES:
- To access items for a nested dictionary, you can use the name of the
  dictionaries, starting with the outer dictionary
'''
# example: (print the name of child 2)
print(myfamily["child2"]["name"])

'''
LOOPING THROUGH NESTED DICTIONARIES:
- You can loop through a dictionary by using the items() method
  like this
'''
# example: (loop through the keys and values of all nested dictionaries)
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
        
# EXERCISE: consider this syntax
        # a = {'name' : 'John', 'age' : '20'}
        # b = {'name' : 'May', 'age' : '23'}
        # customers = {'c1' : a ,'c2' : b}
    # what will be a correct syntax for printing the name 'May'?
# 1.) print(customers['c1']['name']) # correct
# 2.) print(customers.c2.b['name'])
# 3.) print(customers.c2.name)