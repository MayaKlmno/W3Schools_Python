'''
CHANGE LIST ITEMS:

- to change the value of a specific item, refer to the index number:

example:
'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist)

'''
- if you want to change a specific range of elements, define a list with the new values,
and refer to the range of index numbers where you want to insert the new values:
example:
    Change the values "banana" and "cherry" with the values
    "blackcurrant" and "watermelon":
'''
newList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
newList[1:3] = ["blackcurrent", "watermelon"]
print(newList)
'''
- If you insert more items than you replace, the new items will be inserted where you
specified, and the remaining items will move accordingly
example:
'''
anotherlist = ["apple", "banana", "cherry"]
anotherlist[1:2] = ["blackcurrent", "watermelon"]
print(anotherlist)
# in this example we want to put two items in the second interval
# since that is too much, everything after is shifted to make way 
# for this interval
'''
- if you insert less items than you replace, the new items will be inserted where
you specified, and the remaining items will move accordingly:
'''
anotherlist2 = ["apple", "banana", "cherry"]
anotherlist2[1:3] = ["watermelon"]
print(anotherlist2)
# here you said that you were going to be putting two items in the list
# but you only gave one, 
# it says that it will adjust everything accordingly



    
'''
INSERT ITEMS
    - To insert a new list item, without replacing any of the existing values,
    we can use the insert() method
example:
    insert "watermelon" as the third item:
'''
anotherlist3 = ["apple", "banana", "cherry"]
anotherlist3.insert(2, "watermelon")
print(anotherlist3)
'''HOW THE INSERT METHOD WORKS
We can see the first item tells us which place we want to insert it, and the second tells us
what we want to insert
'''

#EXERCISE
# what will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])
# answer -> banana