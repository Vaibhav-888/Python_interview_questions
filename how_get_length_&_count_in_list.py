from collections import Counter

lst = [10, 20, 10, 30, 10, 40]

# 1. using len() function length of list
print(len(lst))

# 2. using count() function to count for specific element in a list
print(lst.count(10))

# 3. using collections.Counter module
counter = Counter(lst)
print(counter) # dictionary of count of elements
# for a specific element
print(counter[10])

# 4. using for loop and condition
counter = 0
for num in lst:
    if num == 10:
        counter += 1
print(counter)