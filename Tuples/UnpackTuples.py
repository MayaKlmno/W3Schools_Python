'''
UNPACK TUPLES:
- When we create a tuple, we normally assign values to it. This is called
  "packing" a tuple:

example: (packing a tuple)
'''
fruits = ("apple", "banana", "cherry") # packing = creating a new tuple

'''
- but in python, we are also allowed to extract the values back into variables.
  This is called "unpacking"
example: (unpacking a tuple)
'''
fruits2 = ("apple", "banana", "cherry")
(green, yellow, red) = fruits2
print(green)
print(yellow)
print(red)
# NOTE: The number of variables must match the number of values in the tuple,
#       if not, you must use an asterisk to collect the remaining values as a list

'''
USING ASTERISK: If the number of variables is less than the number of values, you 
    can add an * to the variable name and the values will be assigned to the variables
    as a list.
example: (assign the rest of the values as a list called "red")
'''
fruits3 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits3
print(green)
print(yellow)
print(red) # this is now a list. everything after value 2 (including) will be a list
# if the asterisk is added to another variable name than the last, Python will
# assign values to the variable until the number of values left matches the 
# number of varaibles left. 
# example: (add a list of values the "tropic variable")
fruits4 = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits4
print(green)
print(tropic) # this one will hold values all the way until the second to last one
        # since the last one will be left for the variable red
print(red)

# EXERCISE: consider the following code:
fruitsExercise = ('maya', 'dean', 'jameson')
(m, d, j) = fruits
print(d)
# what will be the value of y?
# maya
# dean # correct answer
# jameson