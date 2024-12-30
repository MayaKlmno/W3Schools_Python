'''
LIST METHODS:
 - Here are all of the methods relating to lists.
'''
thislist = ["item0", "item1", "item2", "item3", "item4", "item5"]

# APPEND: add an item to the list
thislist.append(1, "appended1")

# CLEAR: removes all the elements from the list
thislist.remove()

# COPY: returns a copy of the list
x = thislist.copy()

# COUNT: returns the number of elements with the specified value
y = thislist.count()

# EXTEND: append items from another list to you current list
    # isn't limited for lists, it can be any iterable object for example a tuple.
extendedList = ["extended0", "extended1", "extended2"]
thislist.extend(extendedList)

# INDEX: returns the index of the first element with the specified value
z = thislist.index("item2")

# INSERT: insert items at a specified index
thislist.insert(3, "inserteditem")

# POP: removes the element at the specified position
thislist.pop(1) # in this example it is the second position

# REMOVE: removes the itme with the specified value
thislist.remove("item3")

# REVERSE: reverses the order of the list
thislist.reverse()

# SORT: sorts the list in a specified order
thislist.sort()