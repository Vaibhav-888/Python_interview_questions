# List Comprehension

lst = [i for i in range(10) if i % 2 == 0]
print(f"By List comp: {lst}")

# syntax: [item for item in range() if condition]

# common way
lst1 = []
for i in range(10):
    if i % 2 == 0:
        lst1.append(i)

print(f"By common way: {lst1}")

