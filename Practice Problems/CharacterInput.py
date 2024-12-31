'''
Exercise 1: Create a program that asks the user to enter their name 
            and their age. 
Print out a message addressed to them that tells them the year that 
            they will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write
            out the year (and therefore be out of date the next year).
'''
name = input("Please enter your name: ")
    # in order to get the input from your user use the input() function
age = input("Please enter your age: ")
    # this variable will now hold the value which the user inputed 
    # in response to the statement
year = input("Before I calculate the year you will turn 100, what year is it?")
timeTo100 = year + (100 - age)
print("Hello " + name + " you will turn 100 in " + timeTo100)


'''
Exercise 2: 
    The exercise comes first, followed by a discussion. Enjoy!
    Ask the user for a number. Depending on whether the number 
    is even or odd, print out an appropriate message to the user. 
    Hint: how does an even / odd number react differently when divided by 2?
'''

number = input("Pick a number!")
if number % 2 == 1:
    print("Why hello there! Such a nice odd number!")
else:
    print("nice even number!")
    

'''
Exercise 3: 
    Take a list, say for example this one:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements
    of the list that are less than 5.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 5:
        print(x)
'''
Extras:
    - Instead of printing the elements one by one,
    make a new list that has all the elements less than 5 from this list
    in it and print out this new list.
    - Write this in one line of Python.
    - Ask the user for a number and return a list that contains only
    elements from the original list a that are smaller than that
    number given by the user.
'''
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = []
# [a.append(x) for x < 5 in b]
for x in b:
    if x < 5:
        a.append(x)
        
'''
EXERCISE 4:
    Create a program that asks the user for a number and then prints out
    a list of all the divisors of that number.
    (If you dont know what a divisor is, it is a number that divides
    evenly into another number. For example, 13 is a divisor of 26
    because 26 / 13 has no remainder.)
'''
userNumber = input("Hi would you please give me the number?")
x = userNumber
while x < userNumber:
    if userNumber % x == 0:
        print(x)
    x = x-1
    
'''
EXERCISE 5:
    Take two lists, say for example these two:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the
    elements that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.
'''
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e = []
for x in c:
    if d.count(x) > 1:
        if e.count(x) == 0:
            e.append(x)
print(e)