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
'''