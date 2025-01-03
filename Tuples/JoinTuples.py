'''
JOIN TWO TUPLES:
- To join two or more tuples you can use the + operator:
example: (join two tuples)
'''
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

'''
MULTIPLY TUPLES:
- If you want to multiply the content of a tuple a given number of times,
  you can use the * operator:
example: (multiply the fruits tuple by 2)
'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits*2  # the list will be one after the other
print(mytuple)

# EXERCISE: what is the correct syntax for joining tuple1
    # tuple2 into tuple3
# tuple3 = join(tuple1, tuple2)
# tuple3 = tuple1 + tuple2   # correct
# tuple3 = [tuple1, tuple2]