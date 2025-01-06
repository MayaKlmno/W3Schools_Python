'''
REMOVE SET ITEMS:
- To remove an item in a set, use the remove(), or the discard() method.
'''
# example: (remove "banana" by using the remove() method)
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
    # I believe that this means that you have to know specifically
    # what value you want to remove
#NOTE: If the item to remove does not exist, remove() will raise an error
    # this means that you have to know what value you want to get rid of first

# example: (remove "banana" by using the discard() method)
thisset2 = {"apple", "banana", "cherry"}
thisset2.discard("banana")
    # this does the same thing as the remove method
    # only with the difference: this will not raise an error if the item doesn't exist
# NOTE: if the item to remove does not exist, discard() will not raise the error

'''
- you can also use the pop() method to remove an item, but this method will remove a 
  RANDOM item, so you cannot be sure what item that gets removed.
    - this is because sets are not ordered, because of that it will remove
      a random item
- The return value of the pop() method is the removed item
'''
# example: (remove a random item by using the pop() method)
anotherset = {"apple", "banana", "cherry"}
x = anotherset.pop()
print(x)
print(anotherset)
# NOTE: sets are unordered, so when using the pop() method, you don't know
      # which item that gets removed

# example: (the clear() method empties the set)
anotherexample = {"apple", "banana", "cherry"}
anotherexample.clear()
print(anotherexample)

# example: (the del keyword will delete the set completely)
anotherset2 = {"apple", "banana", "cherry"}
del anotherset2
# print(anotherset2) # this will cause an error because the set no longer exists

# EXERCISE: what is a correct syntax for removing an item from a set?
# delete()
# remove() # correct
# extract()