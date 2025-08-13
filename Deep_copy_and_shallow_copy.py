# Deep copy

# syntax: copy.deepcopy()
import copy

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"print a is a original object: {a}")

b = copy.deepcopy(a)

b[0][0] = 99

print(f"print b as deepcopy: {b}")
print(f"check if original object is changed after deepcopy: {a}")


# shallow copy

# syntax: copy.copy()

b = copy.copy(a)

b[0][0] = 99
print(f"print b as shallow copy: {b}")
print(f"check if original object is changed after copy: {a}")