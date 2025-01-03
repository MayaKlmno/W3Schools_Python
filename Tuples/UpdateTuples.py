'''
UPDATE TUPLES:
- Tupes are unchangeable, meaning that you cannot add, change, or 
  remove items once the tuple is created. 
  But there are some workarounds


CHANGE TUPLE VALUES:
- Once a tuple is created, you cannot change its value. 
  Tuples are unchangeable, or immutable as it is also called.  
- But there is a workaround. You can convert the tuple into a list, change
  the list, and convert the list back into a tuple.

example: (convert the tuple into a list to be able to change it)
'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

'''
ADD ITEMS:
- Since tuples are immutable, they do not have a built-in append() method,
  but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for chaning a tuple, you
   can convert it into a list, add your item(s), and convert it back into a 
   tuple. 
example: (convert the tuple into a list, add "orange", and convert it back into
a tuple)
'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
'''
2. ADD TUPLE TO A TUPLE: You are allowed to add tuples to tuples, so if
   you want to add one item, (or many), create a new tuple with item(s), and
   add it to the existing tuple:
example: (create a new tuple with the value "orange", and add that tuple:)
'''
anothertuple = ("apple", "banana", "cherry")
z = ("orange",)
anothertuple += z
print(anothertuple)
# NOTE: when creating a tuple with only one item, remember to include a 
#       comma after the item, otherwise it will not be identified as a tuple

'''
REMOVE ITEMS:
- NOTE: you cannot remove items in a tuple
- tuples are unchangeable, so you cannot remove items from it, but
  you can use the same workaround as we used for changing and adding tuple items:
example: (convert the tuple into a list, remove "apple", and convert
          it back into a tuple)
'''
anothertuple2 = ("apple", "banana", "cherry")
a = list(anothertuple2)
a.rempve("apple")
anothertuple2 = tuple(y)
# or you can delete the tuple completely:
# example: (the del keyword can delete the tuple completely)
anothertuple3 = ("apple", "banana", "cherry")
del anothertuple3
# print(anothertuple3) # this will cause an error since the tuple no longer exists

# EXERCISE: You cannot change the items of a tuple, but there are workarounds.
#           Which of the following suggestion will work?

# convert tuple into a list, change item, convert back into a tuple    ## correct
# convert tuple into a set, change item, convert back into a tuple
# convert tuple into a dictionary, change, tiem, convert back into a tuple

