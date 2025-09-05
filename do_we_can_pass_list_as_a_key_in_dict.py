"""
Q. Can we pass a list in a dictionary in python?

No, we cannot use a list as a key in a dictionary because dictionary keys must be hashable
and immutable.

i. lists are mutable (their contents can change), so they are not hashable.
ii. If we try to use a list as key, Python raises a TypeError.

Q. What we can do instead?
Tuples (if all elements inside are immutable) can be used as dictionary keys.

"""

d = {}
try:
    d[[1, 2, 3]] = "value"
except TypeError as te:
    print(te)

# instead we can pass a tuple as a key
d = {}
d[(1, 2, 3)] = "value"
print(d[(1, 2, 3)])


"""
Q. Why can tuples be dictionary keys but not list?
Tuples are immutable and hashable (if only contain immutable items), while lists are mutable
and unhashable.
"""