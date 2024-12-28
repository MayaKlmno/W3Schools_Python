'''
LIST METHODS:
 - Here are all of the methods relating to lists.
'''
thislist = ["item0", "item1", "item2", "item3", "item4", "item5"]

# APPEND: add an item to the list
thislist.append(1, "appended1")

# INSERT: insert items at a specified index
thislist.insert(3, "inserteditem")

# EXTEND: append items from another list to you current list
    # isn't limited for lists, it can be any iterable object for example a tuple.
extendedList = ["extended0", "extended1", "extended2"]
thislist.extend(extendedList)

# INSERT ITEMS: 