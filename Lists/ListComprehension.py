'''
LIST COMPREHENSION:
- List comprehension offers a shorter syntax when
you want to create a new list based on the values of an existing list

example:
    - based on a list of fruits you want a new list containing only the fruits
    with the letter 'a' in the name. 
    Without list comprehension you will have to write a for statement
    with a conditional test inside here is an example of that:
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [] # create a new empty list
for x in fruits: # for loop iterating through each item in the list 'mango'
    if "a" in x: # is statement checking if a is in the item
        newlist.append(x) # adding that item to the new list only if it has the letter a
print(newlist)

# with list comprehension you can do all of that in one line
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

'''
LIST COMPREHENSION SYNTAX:
newlist = [expression for item in iterable if condition == True]
 - the return value is a new list, leaving the old list unchanged.
 
Condition
    - The condition is like a filter that only accepts the item that valuate to True
example: (only accept items that are not "apple")
'''
newlist3 = [x for x in fruits if x != "apple"]
'''
The condition if x != "apple" will return True for all elements other than 'apple'
making the new list contain all fruits except 'apple'
The condition is optional and can be omitted if you want:
example: (with no if statement)
'''
newlist4 = [x for x in fruits]


'''
ITERABLE:
- The iterable can be any iterable object (ex: list, tuple, set)
example: (you can use the range() function to create an iterable)
'''
newlist5 = [x for x in range(10)]
# here is another example, but with a condition:
    # accept only numbers lower than 5:
newlist6 = [x for x in range(10) if x < 5]

'''
EXPRESSION: 
 - the expression is the current item in the iteration, but it is also
 the outcome. you can manipulate it before it ends up like a list item in the new list. 
example: (set the values in the new list to upper case)
'''
newlist7 = [x.upper() for x in fruits]
# this way you can set the outcome to be whatever you want it to be.
# example: (set all the values in the new list to 'hello')
newlist8 = ['hello' for x in fruits]
# the expression can also contain conditions, not like a filter, but as a way to panipulate the outcome:
# example: (return 'orange' instead of 'banana')
newlist9 = [x if x!= "banana" else "orange" for x in fruits]
# the expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange."

#EXERCISE:
# consider the following code:
# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits if x !== 'banana']
# what will be the value of newlist?

# ['apple', 'cherry']
# ['banana']   --> correct answer
# True