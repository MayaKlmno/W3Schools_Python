'''
PYTHON LAMBDA:
A lambda function is a small anonymous function.
A lambda function can take any number of arguments,
    but can only have one expression.
''' 

'''
### Syntax ###
# lambda arguments : expression
#  --- the expression is executed and the result is returned

'''

# example: add to 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

''' Lambda functions can take any number of arguments: '''
# example: multiply argument a with argument b and return the result:
y = lambda a, b : a * b
print(x(5,6))

# example: summarize argument a, b, and c and return the result:
z = lambda a, b, c : a + b + c
print(z(1, 2, 3))


'''
-- WHY USE LAMBDA FUNCTIONS? ---
The power of lambda is better shown when you use them as an anonymous function
    inside another function.
Say you have a function defenition that takes one argument, and that argument
    will be multiplied with an unknown number:
'''

def myfunc(n):
    return lambda a : a * n
    
    # use that function defenition to make a function that always
    # doubles the number you send in:
def myfunc2(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# or, use the same function defenition to make a function that
# always triples the number you send in:
def myfunc2(n):
    return lambda a : a * n
mytripler = myfunc2(3)
print(mytripler(11))

# or, use the same function defenition to make both functions,
# in the same program. 
def myfunction(n):
    return lambda a : a * n
mydoubler1 = myfunction(2)
mytripler1 = myfunction(3)
print(mydoubler1(11))
print(mytripler1(11))

'''
Use lambda function when an anonymouos function is 
required for a short period of time. 
'''

'''
Lambda can take multiple argument, but cannot have multiple expressions
'''