'''
JOINING SETS:
There are several ways to join two or more sets in python.
- The union() and update() methods joins all items from both sets
- The intersection() method keeps ONLY the duplicates
- The difference() method keeps the items from the first set that are not
  in the other set(s)
- The symmetric_difference() method keeps all items EXCEPT the duplicates

UNION:
- The union() method returns a new set with all items from both sets
'''
# example: (join set1 and set2 into a new set)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3= set1.union(set2)
print(set3)
    # this will return a set with all items from both the sets
    
'''
- you can use the | operator instead of the union() method, and you 
  will get the same result
'''
# EXAMPLE: use | to join two sets
anotherset1 = {"a", "b", "c"}
anotherset2 = {1, 2, 3}
anotherset3 = anotherset1 | anotherset2
print(anotherset3)
    # this will return a set with all items from both sets (like the union() method)

'''
JOIN MULTIPLE SETS:
- All the joining methods and operators can be used to join multiple sets. 
- When using a method, just add more sets in the parentheses, spearated by commas
'''
# EXAMPLE: (Join multiple sets with the union() method)
exampleset1 = {"a", "b", "c"}
exampleset2 = {1, 2, 3}
exampleset3 = {"John", "Elena"}
exampleset4 = {"apple", "banana", "cherry"}
myset = exampleset1.union(exampleset2, exampleset3, exampleset4)
print(myset)

# when using the | operator, separate the sets with more | operators:
# example: (use | to join two sets)
aset1 = {"a", "b", "c"}
aset2 = {1, 2, 3}
aset3 = {"John", "Elena"}
aset4 = {"apple", "bananas", "cherry"}

myset2 = aset4 | aset2 | aset3
print(myset2)

'''
JOIN A SET AND A TUPLE:
- The union() method allows you to join a set with other data types,
  like lists or tuples
- This will result in a set
'''
# example: (join a set with a tuple)
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
    # things to note: 
        # the difference of bracket types for sets and tuples
        # this will print a set

# NOTE: The | operator only allows you to join sets with sets, and
#        not with other data types like you can do with the 
#        union() method

'''
UPDATE:
- The update() method inserts all the items from one set into another
- The update() CHANGES the origional set, and does not return a new set
'''
bset1 = {"a", "b", "c"}
bset2 = {1, 2, 3}
bset1.update(bset2)
print(bset1)
    # now bset1 will contain both the components of bset1 and bset2

# example: (the update() method inserts the items in cset2 into cset1)
cset1 = {"a", "b", "C"}
cset2 = {1, 2, 3}
cset1.update(cset2)
print(cset1)
    # now cset1 will contain items from cset1 and cset2
# NOTE: both union() and update() will exclude any duplicate items

'''
INTERSECTION:
- keep ONLY the duplicates
- The intersection() method will return a new set, that only contains the items
  that are present in both sets. 
'''
# example:(join dset1 and dset2, but only keep the duplicates)
dset1 = {"apple", "banana", "cherry"}
dset2 = {"google", "microsoft", "apple"}
dset3 = dset1.intersection(dset2)

# You can use the & operator instead of the intersection() method,
# and you will get the same result. 
# the & and intersection() method are the same/do the same thing

# example: (use & to join two sets)
eset1 = {"apple", "microsoft", "apple"}
eset2 = {"google", "microsoft", "apple"}
eset3 = eset1 & eset2
print(eset3)
# NOTE: the & operator only allows you to join sets with sets, and 
#       not with other data types like you can with the intersection()
#       methods


# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the origional set instead of returning a new set
    # intersection_update() and intersection() method commonality and differences
        # intersection_update() change the origional set
        # intersection() needs/makes a new set

# example: (keep the items that exist in both fset1 and fset2)
fset1 = {"apple", "banana", "cherry"}
fset2 = {"google", "microsoft", "apple"}
fset1.intersection_update(fset2)
print(fset1)
    # see that fset1 is now changed
    
# The values True and 1 are considered the same value.
# The same goes for False and 0
# example: (join sets that contain the values True, False, 1, and 0,
#           and see what is considered as duplicates)
gset1 = {"apple", 1, "banana", 0, "cherry"}
gset2 = {False, "google", 1, "apple", 2, True}
gset3 = gset1.intersection(gset2)
print("this is what gset3 now holds: ")
print(gset3)
    # what this set prints: {False, 1, 'apple'}

'''
DIFFERENCE:
- The difference() method will return a new set that will contain
  only the items from the first set that are not present
  in the other set. 
'''
# example: (keep all items from hset1 that are not in hset2)
hset1 = {"apple", "banana", "cherry"}
hset2 = {"google", "microsoft", "apple"}
hset3 = hset1.difference(hset2)
print(hset3)
    # hset3 will now contain {'banana', 'cherry'}

# You can use the - operator instead of the difference() method, 
#  and you will get the same resutl
# example: (use - to join two sets)
iset1 = {"apple", "banana", "cherry"}
iset2 = {"google", "microsoft", "apple"}
iset3 = iset1 - iset2
print(iset3)
    # this does the same thing as differenct
# NOTE: the - operator only allows you to join sets with sets, and
#       not with other data types like you can with the difference()
#       method

# the difference_update() method will also keep the items from the first
# set that are not in the other set, but it will change the origional
# set instead of returning the new set. 
# example: (use the difference_update() method to keep the items that
#           are not present in both sets)
jset1 = {"apple", "banana", "cherry"}
jset2 = {"google", "microsoft" , "apple"}
jset1.difference_update(jset2)
print(jset1)
    # NOTICE: whenever you use _update() it will change the origional
    # set not, create the new one

'''
SYMMETRIC DIFFERENCES:
- The symmetric_difference() method will keep only the elemetns
  that are NOT present in both sets
'''
# example: (keep the items that are not present in both sets)
kset1 = {"apple", "banana", "cherry"}
kset2 = {"google", "microsoft", "apple"}
kset3 = kset1.symmetric_difference(kset2)
print(kset3)
    # this will now hold: {'banana', 'cherryy', 'google', 'microsoft'}

# you can use the ^ operator instead of the symmertic_difference() method,
# and you will get the same result
# example: (use ^ to join two sets)
lset1 = {"apple", "banana", "cherry"}
lset2 = {"google", "microsoft", "apple"}
lset3 = lset1 ^ lset2
print(lset3)
    # this will now hold: {'banana', 'cherryy', 'google', 'microsoft'}
# NOTE: the ^ operator only allows you to join sets with sets, and 
#       NOT with other data types like you can with the 
#       symmetric_differene method. 

# it looks like whenever you use the shortcuts, you can only use them 
# with sets, not with differing data types


# The symmetric_dfifference_update() method will also keep all the 
# duplicates but it will change the origional set instead of returing a new set
# example: (use the symmetric_difference_update() method to keep
#           the items that are not present in both sets)
mset1 = {"apple", "banana", "cherry"}
mset2 = {"google", "microsoft", "apple"}
mset1.symmetric_difference_update(mset2)

# EXERCISE: what is the correct syntax for joining nset1 and nset2 into nset3
# nset3 = join(nset1, nset2)
# nset3 = nset1 + nset2
# nset3 = nset1.union(nset2)  # correct