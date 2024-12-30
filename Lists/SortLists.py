'''
SORT LIST ALPHANUMERICALLY
- List objects have a sort() method that will sort the list alphanumerically 
    (ascending, by default):
example: (here is the list being sorted alphabetically)
'''
thislistalphabetically = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislistalphabetically.sort()
print(thislistalphabetically)
# when printed it will print:
    # ["banana", "kiwi", "mango", "orange", "pineappe"] --> alphabetically

# the method sort() can also sort it numerically if presented with ints
# here is an example of the list being sorted numerically
thislistnumerically = [100, 50, 65, 82, 23]
thislistnumerically.sort()
print(thislistnumerically)
# the new list holds this:
    # [23, 50, 65, 82, 100]

'''
SOFT DESCENDING:
- to sort descending, use the keyword argument reverse = True:
example: (here is an example using the keyword argument: reverse = True 
    in order to sort the list in descending order)
'''
thislistdescending = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislistdescending.sort(reverse=True)
print(thislistdescending)
# in this example if you put the argument reverse=True in the sort() method
    # sort(reverse=True)
# this is what the list now holds:
    #["pineapple", "orange", "mango", "kiwi", "banana"]


# again you can do the same for reversing the order of ints
# example: (sort the list of ints in descending order)
thislistdescendingnumerically = [100, 50, 65, 82, 23]
thislistdescendingnumerically.sort(reverse=True)
print(thislistdescendingnumerically)
# this list will now hold:
    # [100, 82, 65, 50, 23]


'''
CUSTOMIZE SORT FUNCTION:
- you can also customize your own function by using the keyword argument: 
    key = function
- the function wil return a number that will be used to sort the list (the lowest number first):
example: (sort the list based on how close the number is to 50):
'''
def myfunc(n): # creating your own function
    return abs(n-50) # it gives you how close the number is to 50
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc) # using the argument: key=myfunc
print(thislist)
#  this list's order is now in the order of closest to 50 --> farthest from 50
# this list will now hold: 
    #  [50, 65, 23, 83, 100]
# you can make your own function to sort it in whatever order you want

'''
CASE INSENSITIVE SORT:
- by default the sort() method is case sensitive, resulting in all capital letters being sorted
  before lowercase letters: 
example:
'''
thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort()
print(thislist2)
# you can see that the sort() method is case sensitive which means it sorts the
    # uppercase letterings first, and then the lowercase letterings

# luckily we can use built-in functions as key functions when sorting a list.
# so if you want a case-insensitive sort function, use str.lower as a key function
# example: (preform a case-insensitive sort of the list)
thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist3.sort(key=str.lower)
print(thislist3)
# by using the key function str.lower it will now sort the list without worring about
# the differnt cases


'''
REVERSE ORDER:
- What if you want to reverse the order of a list, regarding the alphabet?
  The reverse() method reverses the current sorting order of the elements
example: (reverse the order of the list items)
'''
thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.reverse()
print(thislist4)
# using the reverse() method, it reverses the orcer that the list is currently in

# EXERCISE:
# what is the correct syntax for sorting a list?
# mylist.order(0)
# mylist.order()
# mylist.sort()  ## correct