'''
REMOVE LIST ITEMS:
- The remove() method removes the specified item.
example: (remove 'banana')
'''
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)
# if there happens to be more item with the value you want removed, then the remove()
# method will remove the first occurance.
# example: (remove the first occurence of banana)
anotherlist = ["apple", "banana", "cherry", "banana", "kiwi"]
anotherlist.remove("banana")
print(anotherlist)


'''
REMOVE SPECIFIED INDEX
- the pop() method removes the specified index.
example: (remove the second item)
'''
anotherlist = ["apple", "banana", "cherry"]
anotherlist.pop(1)
print(anotherlist)
# if you don't specify the index, the pop() method removes the last item.
# Example: (remove the last item)
anotherlist2 = ["apple", "banana", "cherry"]
anotherlist2.pop()
print(anotherlist2)

'''
The del keyword also removes the specified index:
example: (remove the first item)
'''
anotherlist3 = ["apple", "banana", "cherry"]
del anotherlist3[0]
print(anotherlist3)
# the del keyword can also delete the list completely
# example (delete the entire list)
anotherlist4 = ["apple", "banana", "cherry"]
del anotherlist4

'''
CLEAR THE LIST:
The clear() method empties the entire list.
The list will still remain, but it will have no content.
example: (clear the list content)
'''
anotherlist5 = ["apple", "banana", "cherry"]
anotherlist5.clear()
print(anotherlist5)

# EXERCISE: 
# what is the list method for removing list items
# pop()