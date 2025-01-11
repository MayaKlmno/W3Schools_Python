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