'''
PYTHON CONDITIONS AND IF STATEMENTS:
- Python supports the usual logical conditions from mathematics:
    - equals: a == b
    - not equals: a != b
    - less than: a < b
    - less than or equal to: a <= b
    - greater than: a > b
    - greater than or equal to: a >= b
- these conditions can be used in several ways, most commonly in "if statements and loops"
- an "if statement" is written by using the if keyword
'''
# example: (if statement)
a = 33
b = 200
if b > a:
    print("b is greater than a")

'''
- In this example we use two variables, a and b, which are used as part
  of the if statement to test whether b is greater than a. As a is 33,
  and b is 200, we know that 200 is greater than 33, and so we print that
  "b is greater than a"
'''

'''
INDENTATION:
- python relies on indentaiton to define the scope of the code. 
  other programming languages often use curly-brackets for this 
  purpose. such as java
'''
# example 
    # if you write an if statement with improper indentaion an 
    # error will arise
    
'''
ELIF:
- the elif keyword is python's way of saying:
  "if the previous conditions were not true, then try this conditon"
'''
# example:
c = 33
d = 33
if b > a:
    print("d is greater than c")
elif a == b:
    print("c and d are equal")

# in this example a is equal to b, so the first conditon is
# not true, but the elif condition is true, so we print to screen
# that "a and b are equal" 

'''
ELSE:
- The else keyword catches anything which isn't cought
  by the preceding conditions
'''
# example:
e = 200
f = 33
if f >  e:
    print("f is greater than e")
elif e == f:
    print("e is equal to f")
else:
    print("a is greater than b")
# in this example e is greater than f, so the first condition is false,
# the elif conditon is also false, so we have to go to the else condtion
# and print to screen that "a is greater than b"

# you can also have the else without the elif
g = 200
h = 33
if h > g:
    print("h is greater than g")
else:
    print("h is not greater than g")
    
'''
SHORT HAND IF:
- if you have only one statement to execte, you can put it on the same line
  as the if statement
'''
# example: (one line if statement)
if a > b: print("a is greater than b")

'''
SHORT HAND IF... ELSE:
- if you have only one statement to execute, on for if, and one for else,
  you can put it all on the same line
'''
# example: (one line if else statement)
aa = 2
bb = 330
print("A") if aa > bb else print("B")

## This technique is known as ternary operators, or conditional expressions
# You can also have multiple else statements on the same line:

# example: (one line if else statement, with 3 conditions)
aaa = 330
bbb = 330
print("A") if aaa > bbb else print("=") if aaa == bbb else print("B")

'''
AND:
- The and keyword is a logical operator, and is used to combine conditional
  statements
'''
# example: (Test if a is greater than b, AND if c is greater than a)
a1 = 200
b1 = 33
c1 = 500
if a1 > b1 and c1 > a1:
    print("Both conditions are True")
    
'''
OR:
- The or keyword is a logical operator, and is used to combine conditonal
  statements
'''
# example: (test if a is greater than b, OR if a is greater than c)
a2 = 200
b2 = 33
c2 = 500
if a2>b2 or a2>c2:
    print("At leas one of the conditions is True")

