lst = [1, 2, 2, 3, 4, 4, 5]

# 1. using set() method
print(list(set(lst)))

# 2. using dict.fromkeys()
unique_list = list(dict.fromkeys(lst))
print(unique_list)

# 3. using for loop and condition
unique_numbers = []
for num in lst:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

# 4. using list comprehension of the above for loop
unique_numbers1 = []
# list comp syntax: [item for item in iterable if condition]
[unique_numbers1.append(num) for num in lst if num not in unique_numbers1]
print(unique_numbers1)