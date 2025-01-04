myset = {"apple", "banana", "cherry"}

'''
SET:
- Sets are used to store multiple items in a single variable. 
- Set is one of the 4 built-in data types in Python used to store collections
  of data, the other 3 are List, Tuple, and Dictionary, all with different
  qualities and usage. 
- A set is a collection which is unordered, unchangeable, and unindezed
NOTE: Set items are unchangeable, but you can remove items and add new items
- Sets are writtien with curly brackets
example: (create a set)
'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
# NOTE: sets are unordered, so you cannot be sure in which order the 
# items appear.

'''
SET ITEMS:
- Set items are unordered, unchangeable, and do not allow duplicate values
        # if a duplicate item is presented, it doesn't show up

UNORDERED: 
- Unordered means that the items in a set do not have a defined order.
- Set items can appear in a different order every time you use them,
  and CANNOT be referred to by index or key
  
UNCHANGEABLE:
- Set items are unchangeable, meaning that we cannot change the items
  after the set has been created

# NOTE: Once a set is created, you cannot change its items, but you can
# remove items and add new items

DUPLICATES NOT ALLOWED:
- Sets CANNOT have two items with the same value
example: (duplicate values will be ignored)
'''
anotherset = {"apple", "banana", "cherry", "apple"}
print(anotherset) 
    # as you can see the secon capple is not accounted for.
    # its also unordered so when printed, its not printed in the order
    # which we wrote it
    
# NOTE: the values True and 1 are considered the same values in sets,
#       and are treated as duplicates:
# example: (True and 1 is considered the same value)
thisset2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset2)
    # As you can see instead of having both 1 and True, it only prints
    # out the 1. 
    # Additionally it is not in a specified order.
# NOTE: the values False and 0 are considered the same value in sets,
#       and are treated as duplicates
# example: (Fase and 0 is considered the same value)
anotherset2 = {"apple", "banana", "cherry", False, True, 0}
print(anotherset2)
    # As you can see it only includes False, not both false and 0
    # additionally the order keeps on changing
    
'''
GET THE LENGTH OF A SET:
- To determine how many items a set has, use the len() function
example: (get the number of items in a set)
'''
anotherset3 = {"apple", "banana", "cherry"}
print(len(anotherset3))
    # use the len() function for all three: lists, tuples, and sets

'''
SET ITEMS - DATA TYPES:
- Set items can be of ANY data types:
example: (String, int, and boolean data types)
'''
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# NOTE: a set CAN contain DIFFERENT data types:
# example: (a set with strings, integers, and boolean values)
aset1 = {"abc", 34, True, 40, "male"}
