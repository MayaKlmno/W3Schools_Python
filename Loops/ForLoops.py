'''
PYTHON FOR LOOPS:
- A for loop is used for iterating over a sequence (that is 
  either a list, a tuple, a dictionary, a set, or a string)
- This is less like the for keyword in other programming lanugages,
  and works more like an iterator method as found in other
  object-orienated programming languages.
- With the for loop we can execute a set ofstatements, one
  for each item in a list, tuple, set, etc.
'''
# example: (print each fruit in a fruit list:)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# the for loop doesn't require an indexing variable to be set beforehand
    # it indexes until the list is finished (or something else)


'''
LOOPING THROUGH A STRING:
- Even strings are iterable objects, they contain a sequence of characters:
'''
# example: (loop through the letters in the word "banana")
for x in "banana":
    print(x)
    # in this one it loops through the different characters in the word banana

'''
THE BREAK STATEMENT:
- with the break statement we can stop the loop before it has looped through all the items
'''
# example: