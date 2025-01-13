'''
PYTHON LOOPS:
- Python has two primitive loop commands:
    - while loops
    - for loops
'''

'''
THE WHILE LOOP:
- With the while loop we can execute a set of statements as long as the condition
  is true.
'''
# example: (Print i as long as i is less than 6)
i = 1
while i < 6:
    print(i)
    i += 1

# NOTE: remember to increment i, or else the loop will continue forever

# The while loop requires relevent variables to be ready, in this example we need
# to define an indexing variable, i, which we set to 1

'''
THE BREAK STATEMENT:
- With the break statement we can stop the loop even if the while condition
  is true:
'''
# example: (exit the loop when i = 3)
x = 1
while x < 6:
    print(x)
    if x == 3:
        break
    x += 1

'''
THE CONTINUE STAEMENT:
- With the continue statement we can stop the current iteration, and continue
  with the next:
'''
# example: (continue to the next iteration if i = 3)
y = 0
while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)

'''
THE ELSE STATEMENT:
- print a message once the condition is false
'''
z = 1
while z < 6:
    print(z)
    z += 1
else:
    print("i is no longer less than 6")
    
## EXERCISE: which statement is a correct syntax to break out of a loop
# end
# return
# break  ## correct