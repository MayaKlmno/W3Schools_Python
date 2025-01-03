'''
LOOP TUPLES: 
- You can loop through the tuple items by using a for loop
example: (iterate through the items and print the values)
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

'''
LOOP THROUGH THE INDEX NUMBERS:
- You can also loop through the tuple items by referring to their index number.
  Use the range() and len() functions to create a suitable iterable. 
example: (print all items by referring to their index number)
'''
anothertuple = ("apple", "banana", "cherry")
for i in range(len(anothertuple)):
    print(anothertuple[i])


'''
USING A WHILE LOOP:
- you can loop through the tuple items by using a while loop.
- Use the len() function to determine the length of the tuple, then
  start at 0 and loop your way through the tuple items by referring to 
  indexes.
- Remember to increase the index by 1 after each iteration.
example: (print all items, using a while loop to go through all the 
    index numbers)
'''
thistuple2 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple2):
    print(thistuple2[i])
    i = i+1

# EXERCISE: What is a correct syntax for looping through the items of a tuple?

# 1 for x in ('apple', 'banana', 'cherry'):
#     print(x)       # correct
# 2 for x in ('apple', 'banana', 'cherry'):
#       print(x)
# 3 foreach x in ('apple', 'banana', 'cherry'):
#       print(x)