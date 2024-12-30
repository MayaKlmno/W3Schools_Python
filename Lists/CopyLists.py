'''
COPY LISTS:
- You cannot copy a list simply by typing list2 = list1
because list2 will only be a reference to list1, and changes
made in list1 will automatically also be made in list2.

USE THE COPY() METHOD
- you can use the built-in List method copy() to copy a list
example: (make a copy of a list with the copy() method)
'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
    # another way to make a copy is to use the built-in method list()
# example: (make a copy of alist with the list() method)
thislist2 = ["apple","banana", "cherry"]
mylist2 = list(thislist2)
print(mylist2)

'''
USE THE SLICE OPERATOR
- you can also make a copy of a list by using the : (slice) operator
example: (make a copy of a list with the : operator)
'''
thislist3 = ["apple", "banana", "cherry"]
mylist3 = thislist3[:]
print(mylist3)