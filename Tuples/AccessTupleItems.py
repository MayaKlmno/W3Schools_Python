'''
ACCESS TUPLE ITEMS:
- You can access tuple items by referring to the index
  number, inside square brackets:
example: (print the second item in the tuple)
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# remember that the indexes start at 0

'''
NEGATIVE INDEXING:
- Negative indexing means start from the end (like for lists)
  -1 refers to the last item, -2 refers to the second last item etc
example: (print the last item of the tuple)
'''
anothertuple = ("apple", "banana", "cherry")
print(anothertuple[-1])
    # this will print: cherry
    
'''
RANGE OF INDEXES:
- You can specify where to start and where to end the range
- When specifying a range, the return value will be a new tuple 
  with the specified items. 
example: (return the third, fourth, and fifth item)
''' 
anothertuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon",
                 "mango")
print(anothertuple2[2:5])
    # note: the search will start at index 2 (including it) and end
    # at index 5 (not included)
    # remember that the first item has index 0

# when you leave out the start value, the range will start at the first
# item
# example: (this example returns the items from the beginning to,
# # but NOT included, "kiwi")
anothertuple3 = ("apple", "banana", "cherry", "orange", "kiwi", 
                 "melon", "mango")
print(anothertuple3[:4]) 
        # when you don't include the first value, it will start from the 
        # begining

# you can go to the end of the tuple by leaving out the end of the 
# tuple:
# example: (this example returns the items from "cherry" to the end)
anothertuple4 = ("apple", "banana", "cherry", "orange", "kiwi",
                 "melon", "mango")
print(anothertuple4[2:])
    # this goes right to the end
    

'''
RANGE OF NEGATIVE INDEXES:
- specify negative indexes if you want to start the search
  from the end of the tuple:
example: (this example returns the item from index -4 (included) to index -1(excluded))
'''
anothertuple5 = ("apple", "banana", "cherry", "orange", "kiwi",
                 "melon", "mango")
print(anothertuple5[-4,-1])


'''
CHECK IF AN ITEM EXISTS:
- to determine if a specified item is present in a tuple
  use the in keyword:
example: (check if "apple" is present in the tuple)
'''
thistuple2 = ("apple", "banana", "cherry")
if "apple" in thistuple2:
    print("yes 'apple' in the tuple")