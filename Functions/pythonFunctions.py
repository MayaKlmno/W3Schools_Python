'''
PYTHON FUNCTIONS:
- A function is a block of code which only runs when it is called
- You can pass data, known as parameters, into a function
- A function can return data as a result

CREATING A FUNCTION:
- in python a function is defined using the def keyword
'''
# example:
def myfunction():
    print("Hello from a function")

'''
CALLING A FUNCTION:
- To call a function, use the function name followed by parenthesis:
'''
# example:
myfunction()

'''
ARGUMENTS:
- Information can be passed into funcitons as arguments
- Arguments are specified after the funciotn name, inside the parentheses. 
  You can add as many arguments as you want, just separate them with a comma. 
- The following example has a function with one argument (fname). 
  When the function is called, we can pass along a first name, which is
  used inside the funtion to print the full name:
'''
# example:
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobaias")
my_function("Jameson")
    # Arguments are often shortened to args in Pythton documentations
    
'''
PARAMETERS OR ARGUMENTS:
- The terms parameter and argument can be used foir the same thing: Information that are passed
  into a function

from a functions perspective:
    - a parameter is the variable listed inside the parentheses in the function definition
    - an argument is the value that is sent to the function when it is called 

NUMBER OF ARGUMENTS:
- By default a funciton must be called with the correct number of arguments.
  Meaning, that if your function expects 2 arguments, you have to call the function
  with 2 arguments.
'''
# example: (this function expects 2 arguments, thus gets 2 arguments)
def my_function2(fname, lname):
  print(fname + " " + lname)
my_function2("Dean", "Redding")
  # if you try to call the function with 1 or 3 arguments you will get an error

'''
ARBITRARY ARGUMENTS, *args
- If you do not know how many arguments that will be passed into your function,
  add a * before the parameter name in the function definition
- This way the function will receive a tupe of arguments, and can access
  the items accordingly
'''
# example: (if the number of arguments is unknown, add a * before the parameter name:)
def another_function(*kids):
  print("The youngest child is " + kids[2])
another_function("Dean", "Jameson", "arron")  
  # arbitrary arguments are often shortened to *args in Python documentations

'''
KEYWORD ARGUMENTS:
- You can also send arguments with the key = value syntax
- This way the order of the arguments does not matter
'''
# example:
def example_function(child3, child2, child1):
  print("The youngest child is " + child3)
example_function(child3="dean", child2="jameson", child1="aaron")
  # the phrase Keyword Arguments are often shortened to kwargs in Python

'''
ARBITRARY KEYWORD ARGUMENTS **kwargs
- if you do not know how many keyword arguments that will be passed
  into your function, add two asterisk: ** before the parameter name
  in the function definition
- this way the function will receive a dictionary of arguments and can
  acces the items accordingly
'''
# example: (if the number of keyword arguments is unknown, add a double **
#   before the parameter name)
def here_function(**kid):
  print("His last name is " + kid[lname])
here_function(fname = "Jameson", lname = "Hawthorne")
  # arbitrary Kword arguments are often shortened to **kwargs in python
  # documentations
  
'''
DEFAULT PARAMETER VALUE
- The following example shows how to use a default parameter value
- if we call the function without argument, it uses the default value
'''
# example:
def hi(country = "England"):
  print("I am from " + country)
hi("Sweeden")
hi("Romania")
hi()
hi("France")

'''
PASSING A LIST AS AN ARGUMENT:
- You can send any data types of argument to a function (string,
  number, list, dictionary, etc.)
  and it will be treated as the same data type inside the function
- eg: if you send a list as an argument, it will still be a List when
  reaches the function
'''
# example:
def hello(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
hello(fruits)

'''
RETURN VALUES:
- to let a function return a value, use the return statement
'''
# example: 
def function(x):
  return 5*x
print(function(3))
print(function(5))
print(function(9))

'''
THE PASS STATEMENT:
- functioon definitions cannot be empty, but if you for some reason
  have a function definition with no content, put in the pass statement
  to avaoid getting an error
'''
# example:
def hey():
  pass

'''
POSITIONAL-ONLY ARGUMENTS:
- You can specify that a function can have ONLY positional arguments or ONLY keyword
  arguments
- To specify that a function can have only positional arguments, add , / after the 
  arguments 
'''
# example
def my_function(x, /):
  print(x)
my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if
# the function expects positional arguments
# example
def here(x):
  print(x)
here(x=3)

# But when adding the , / you will get an error if you try to send a keyword argument:
'''
# wrong
def my_function(x, /):
  print(x)
my_function(x=3)
'''

'''
KEYWORD-ONLY ARGUMENTS:
To specify that a function can have only keyword arguments, add *, before the arguments:
'''
#Example
def my_function3(*,x):
  print(x)
my_function3(x=3) ### must put x =    or else you would get an error
'''
Without the *, you are allowed to use positional arguments even if the function expects
keyword arguments
'''
#Example:
def my_function4(x):
  print(x)
my_function4(3)

##!! BUT with the *, you will get an error if you try to send a positional argument:

'''
COMBINE POSITIONAL-ONLY AND KEYWORD-ONLY:
You can combine the two argument types in the same function.
Any argument before the / , are positional-only, and any argument after the *, are keyword only
'''
#Example:
def my_function5(a,b, /, *, c,d):
  print(a+b+c+d)
my_function5(5,6,c=7, d=8)

'''
RECURSION:
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a 
function that never terminates, or one that uses excess amounts of memory or processor power.
However, when written correctly recursion can be a very efficient and mathematically-elegent way
to approach to programming.

In this example, tri_recursion() is a function that we have defnined to call itself ("recurse").
We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when
the condition is not greater than 0 (i.e. when it is 0)

To a new developer it can take4 some time to work out how exactly this works, best way to find out is 
by testing and modifying it.
'''
#Example:
def tri_recursion(k):
  if(k>0):
    result = k + tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)
'''
  The result:
    Recursion Example Results:
    1
    3
    6
    10
    15
    21
'''