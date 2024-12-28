'''
Access Items:
- List items are indexed and you can access them by referring to the index number
  starting at index of 0 for the first element
  
Negative Indexing:
- means start from the end
-1 refers to the last item, -2 refres to the second last item etc
'''
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# will print cherry

'''
Range of Indexes:
- you can specify a range of indexes by specifiying where to start
and where to end the range
- when specifying a range, the return value will be a new list with the specified items
'''
#example: return the thirsd fourth and fith item:
exampleList = ["apple", "banana", "cherry", " orange", "kiwi", "melon", "mango"]
print(exampleList[2:5])

'''
- if you want to the range to start from the begining, then you can just leave out he start
value
example:
'''
print(exampleList[:4])

'''
- if you want to range all the way to the end then just leave
out the end value
example:
'''
print(exampleList[2:])

'''
- you can also do a range for negative indexes
- specify negative indexes if you want to start the search from the end of the list:
'''
print(exampleList[-4:-1])

'''
CHECK IF ITEM EXISTS:   
- to determine if a specified item is present in a list use the in keyword:
example:
    - ceck if "apple" is present in the list:
'''

if "apple" in exampleList:
    print("Yes, 'apple' is in the fruits list")

#Exercise
# what will be printed from the following syntax:
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])
#cherry