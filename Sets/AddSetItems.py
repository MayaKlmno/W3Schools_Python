'''
ADD ITEMS:
- Once a set is created, you cannot change its items,
  but you can add new items. 
- To add one item to a set use the add() method
'''
# example: (add an item to a set, using the add() method)
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
    # now the set will include orange at the end

'''
ADD SETS:
- To add items from another set into the current set,
  use the update() method
'''
# example: (add elements from tropical into thisset2)
thisset2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset2.update(tropical)
print("thisset2: ")
print(thisset2)
    # the new list will contain both lists, unordered

'''
ADD ANY ITERABLE:
- The object in the update() method does not have to be
  a set, it can be any iterable object (tuple, lists, dictionaries etc)
'''
# example: (add elements of a list to a set)
thisset3 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset3.update(mylist)
print(thisset3)
    # this will do the same thing as the example above
    # even though it is a list

# EXERCISE: What is the correct syntax for adding items to a set
# add() # correct
# insert()
# push()