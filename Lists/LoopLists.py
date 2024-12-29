'''
LOOPING THOUGH A LIST:
- You can loop through a list using the FOR LOOP
example: (Print all the items in the list, one by one)
'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
'''
comparison with java: (the java for loop)
    for(i = 0; i < thislist.length(); i++){
        print(thislist[i])
    }
some differences:
    - the header goes through all of the items inside the list
    - x is the item itself in the list while i is just a number
    - the python one doesn't have parenthesis but it has :
'''    

'''
LOOP THROUGH INDEX NUMBERS:
- you can also loop through the list items by referring to their 
index number. use the range() and len() functions to create a suitable
iterable. 
example: (print all items by referring to their index number.)
'''
anotherlist = ["apple", "banana", "cherry"]
for i in range(len(anotherlist)):
    print(anotherlist[i])
# as you can see this one is closer to my python example
# the iterable created in the example above is [0,1,2]



'''
USING A WHILE LOOP:
- You can loop through the list items by using a while loop. 
- Use the len() function to determine the length of the list, then start
at 0 and loop your way through the list items by referring to their indexes. 
- Remember to increase the index by 1 after each iteration, or else it will
result in an infinate loop. 
Example: (print all items, using a while loop to go through all the index numbers)
'''
anotherlist2 = ["apple", "banana", "cherry"]
i = 0 # create the variable 1
while i < len(thislist): # it will keep on going until i is less than the length of the list
    print(anotherlist2[i]) 
    i = i+1 # make sure it doesn't do an infinate loop
  
##### IMPORTANT BECAUSE I HAVE NOT LEARNED ANYTHING LIKE THIS BEFORE ##########  
'''
LOOPING USING LIST COMPREHENSION:
- List comprehension offers the shortest syntax for looping through lists:
example: (a shorthand for loop that will print all items in a list)
'''
anotherlist3 = ["apple", "banana", "cherry"]
[print(x) for x in anotherlist3]
######## ###########

# EXERSISE 
'''
what is the correct synax for looping through the items of a list? 
1.) 
    for x in ['apple', 'banana', 'cherry']:
        print(x) ### correct answer
2.)
    for x in ['apple', 'banana', 'cherry']:
        print(x)
3.)
    foreach x in ['apple', 'banana', 'cherry']
        print(x)
'''