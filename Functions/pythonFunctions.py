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
# example: (if the number of arguments is unknown )