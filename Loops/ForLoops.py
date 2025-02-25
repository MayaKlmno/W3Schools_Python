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
# example: (exit the loop when x is "banana")
fruits2 = ["apple", "banana", "cherry"]
for x in fruits2:
    print(x)
    if x == "banana":
        break
    
# example: (exit the loop when x is "banana", but this time the break comes before the print)
fruits3 = ["appple", "banana", "cherry"]
for x in fruits3:
    if x == "banana":
        break
    print(x)
    
'''
THE CONTINUE STATEMENT:
- with the continue statement we can stop the current iteration of the loop and continue
  with the next
'''
# example: (do not print banana)
fruits4 = ["apple", "banana", "cherry"]
for x in fruits4:
    if x == "banana":
        continue
        # this will result in not printing banana
    print(x)
    
'''
THE RANGE() FUNCTION:
- To loop through a set of code a specified number of times, we can use the range() function
- The range() function returns a sequence of numbers, starting from 0 by default, and increments
  by 1 (by default), and ends at a specified number
'''
# example: (use the range() function)
for x in range(6):
    print(x)
    # note that range(6) is not the values of 0 to 6 but the values 0 to 5
    
'''
- the range() function defaults to 0 as the starting value, however it is possible to specify 
  the starting value by adding a parameter: range(2, 6), which means values from 2 to 6
  (but not including 6)
'''
# example: (using the start parameter)
for x in range(2,6):
    print(x)

# the range() function defaults to increment the sequence by 1, however it is possible to specify
# the increment value by adding a third parameter: range(2, 30, 3)
# example: (increment the sequence with 3 (default is 1))
for x in range(2, 30, 3):
    print(x)
    
    
'''
ELSE IN FOR LOOP:
- The else keyword in a for loop specifies a block of code to be executed
  when the loop is finished
'''
# example: (print all numbers from 0 to 5 and print a message when 
#           the loop has ended)
for x in range(6):
    print(x)
else:
    print("finally finished!")

# NOTE: the else block will NOT be executed if the loop is stopped by
#       a break statement
# example: (break the loop when x is 3, and see what happens with the else block)
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("finally finished")
    
'''
NESTED LOOPS:
- A nested loop is a loop inside a loop.
- the "inner loop" will be executed one more time for each iteration of the "outer loop"
'''
# example: (print each adjetive for every fruit)
adj = ["red", "big", "tasty"]
fruits5 = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits5:
        print(x, y)

'''
THE PASS STATEMENT:
- for loops cannot be empty, but if you for some reason have a for loop with no content,
  put in the pass statement to avoid getting an error
'''
for x in [0, 1, 2]:
    pass

# EXERCISE: what will be the result of the following code:
for x in range(3):
    print(x)
# 1: 0 1 2  # correct
# 2: 0 1 2 3
# 3: 1 2 3