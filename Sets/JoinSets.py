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