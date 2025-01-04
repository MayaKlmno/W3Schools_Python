'''
ACCESS ITEMS:
- You cannot access items in a set by referring to an
  index or a key.
- But you can loop through the set items using a for loop
  or ask if a specified value is present in a set,
  by using the in keyword. 
'''
# example: (Loop through the set, and print the values)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# example: (check if 'banana' is present in the set)
thisset2  = {"apple", "banana", "cherry"}
print("banana" in thisset2)
    # will print out true
    # because banana is in the set

# example: (check if "banana" is NOT present in the set)
thisset3 = {"apple", "banana", "cherry"}
print("banana" not in thisset3)
    # will print out false
    # because banana is in the set

'''
CHANGE ITEMS: 
- once a set is created, you cannot change its items, but you can add new items
'''

# EXERCISE: True or False. You can acces set items by referring to the index
# false