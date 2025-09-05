"""
Q1: can we pass a list in a tuple?

Yes, you can pas a list as an element inside a tuple in python. 

A tuple is immutable, meaning you cannot change or reassign its elements once it's created. But if
a tuple contains a mutable object like a list, the contents of that can still be modifies.

Q2. If tuples means you cannot reassign or remove tuple elements, but if an element is a mutable
object (like a list or dict), that object's contents can be modified.
"""

# Q1 example:
t = (1, 2, [1, 2])
print(t)

t[2].append(8)
print(t)

# Q2 example
def test_list_in_tuple():
    t = (1, 2, [3, 4])
    t[2].append(5)
    assert t == (1, 2, [3, 4, 5])

test_list_in_tuple()