'''
JOIN LISTS:
Join two lists:
- there are several ways to join, or concatenate two or more lists in python
the simpilest is to use the + operator
example: (join two lists)
'''
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 # conatinating the two lists
print(list3)
# unlike java you can easily conatenate ints and strings

# another way to join two lists is by appending all the items from list2
    # into list 1, one by one:
# example: (append list4 into list5)
list4 = ["a", "b", "c"]
list5 = [1, 2, 3]
for x in list5:
    list4.append(x)
print(list4)
# list4 will now include what list 4 origionally had and 
    # what list5 had right after it

# or you can use the extend() method, where the purpose is to add elements
# from one list to another list:
# example: (use the extend() method to add list7 at the end of list6)
list6 = ["a", "b", "c"]
list7 = [1, 2, 3]
list6.extend(list7)
print(list6)
# list6 will now include list7 right after

# EXERCISE:
# what is the correct syntax for joining list1 and list2 into list3
# list3 = join(list1, list2)
# list3 = list1 + list2 # correct
# list3 = [list1, list2]