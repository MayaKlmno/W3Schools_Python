'''
LIST:
    - Lists are used to store multple items in a single variable
    - List's index start at 0
    - lists are ordered
        - have a definied order and will not change that order
        - can have list methods to change the order though
    - since the lists are indexed they can have multiple of the same value
    

an example list is below
'''
# constructing a list method 1
thislist = ["item0", "item1", "item2"]
print(thislist)
# constructing a list method 2
    # using the list() constructor
mylist = list(("apple","banana","cherry"))
    # notice the double round brackets


'''
DATA TYPES:
    - the methdos can be of any datatypes
    - examples:
        string, int, boolean
    - the list can also contain multiple methods inside one list
'''

'''
IMPORTANT METHODS:
'''
#List Lengths (len method):
print(len(thislist))

#Type: (to figure out what type of list you have)
print(type(thislist))

'''
PYTHON COLLECTIONS (ARRAYS):
- List: a collection which is ordered and changable. Allows dupicate members
- Tuple: a collection which is ordered and unchangable. Allows dupicate members
- Set: a collection which is unordered, unchangable, and unindexed. No duplicate members.
- Dictionary: a collection which is ordered and changable. No duplicate members
'''

'''
Exercise:
- what will be the result of the following syntax:
'''
exerciseList = ['apple', 'banana', 'cherry']
print(exerciseList[1])
# banana