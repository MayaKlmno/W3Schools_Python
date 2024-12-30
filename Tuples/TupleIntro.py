'''
TUPLES:
- Tuples are used to store multiple items in a single variable.
- Tuple is one of 4 built-in data types in Python used to store
  collections of data, the other 3 are List, Set, and Dictionary,
  all with different qualities and usage.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets
example: (create a Tuple)
'''
mytuple = ("apple", "banana", "cherry")
print(mytuple)

'''
TUPLE ITEMS:
- Tuple items are ordered, unchangeable, and allow duplicate values
- Tuple items are indexed, the first item has index [0],
  the second item has index [1] etc

ORDERED:
- When we say that tuples are ordered, it means that the items
  have a defined order, and that order will not change.

UNCHANGEABLE:
- Tuples are unchangeable, meaning that we cannot change,
  add or remove items after the tuple has been created.
  
ALLOW DUPLICATES:
- Since tuples are indexed, they can have items with the same value:
example: (tuples allow duplicate values:)
'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

'''
TUPLE LENGTH:
- To determine how many items a tuple has, use the len() function
example: (print the number of items in the tuple:)
'''
thistuple2 = ("apple", "banana", "cherry")
print(len(thistuple2)) # note that tupes also use the len functions
    # like the lists

'''
CREATE TUPLE WITH ONE ITEM:
- to create a tuple with only one item, you must add a comma
  after the item, otherwise Python will not recognize it
  as a tuple.
example: (one item tuple, rememebr the comma)
'''
thistuple3 = ("apple",)
print(type(thistuple3))
# NOT A TUPLE:
thistuple4 = ("apple")
print(type(thistuple4))

'''
TUPLE ITEMS - DATA TYPES:
- tuple items can be of any data type:
example: (String, int and boolean data types)
'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
# example: (a tuple with strings, ints, and boolean values)
tuple4 = ("abc", 34, True, 40)

'''
TYPE()
- from python's perspective, tuples are defined as objects
  with the data type 'tuple':
<class 'tuple'>
example: (what is the data type of a tuple)
'''
anothertuple = ("apple", "banana", "cherry")
print(type(anothertuple))

'''
THE TUPLE() CONSTRUCTOR:
- It is also possible to use the tuple() constructor to
  make a tuple
example: (using the tuple() method to make a tuple)
'''
anothertuple2 = tuple(("apple", "banana", "cherry"))
    # note the double round-brackets
print(anothertuple2)

'''
PYTHON COLLECTIONS (ARRAYS):
- There are four collection data types in python
    - List: a collection which is ordered and changeable
        allows duplicate memebers.
    - Tuple: a collection which is ordered and unchangeable
        allows duplicate members
    - Set: a collection which is unordered, unchangeable, and
        unindexed. No duplicate members
    - Dictionary: a collection which is ordered and changeable
        no duplicate members
        
- set items are unchangeable, but you can remove and/or
  add items whenever you like
- when choosing a collection type, it is useful to understand
  the properties of that type. 
- choosing the right type for a particualr data set could mean
  retention of meaning, and, it could mean an increase in 
  efficiency or security.
'''

# EXERCISE:
# which one of these is a tuple?
# thistuple = ('apple', 'banana', 'cherry')  # correct
# thistuple = ['apple', 'banana', 'cherry']
# thistuple = {'apple', 'banana', 'cherry}