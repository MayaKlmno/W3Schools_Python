'''
APPEND ITEMS:
- to add an item to the end of the list use the append() method:
example: (of using the append() method)
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

'''
INSERT ITEMS:
- To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:
example:
'''
anotherlist = ["apple", "banana", "cherry"]
anotherlist.insert(1,"orange")
print(anotherlist)
# as a resutl of the examples above, the lists will now contain 4 items

'''
EXTEND LIST:
- To append elements from another list to the current list, use the extend() method
example: (add the elements of tropical to extenedlist)
'''
extendedList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
extendedList.extend(tropical)
print(extendedList)
# in this example the elements from tropical will be added to the 
# end of the extendedList list.

'''
ADD ANY ITERABLE:
- the extend() method does not have to append lists, you can add any iterable object
(tuples, sets, dictionaries, etc.)
example: (add elements of a tuple to a list)
'''
thislist2 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist2. extend(thistuple)
print(thislist2)

# Exercise:
# what will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])
# apple