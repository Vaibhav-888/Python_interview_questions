# convert a nested list into flat list

# how to do it?

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1. Using nested loop

def flatten_list(nested_list):
    flatList = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)

    return flatList

if __name__ == "__main__":
    print(f"nested_list: {nested_list}")
    print(f"flatten list: {flatten_list(nested_list)}")

# 2. Using a list comprehension
flattened_list = [element for innerList in nested_list for element in innerList]
print(f"flattened_list using list_comp: {flattened_list}")

# 3. Using recursion
flat_list = []
def removeNesting(nested_list):
    for innerList in nested_list:
        if type(innerList) == list:
            removeNesting(innerList)
        else:
            flat_list.append(innerList)
    return flat_list
print(f"Flattened_list using recursion: {removeNesting(nested_list)}")


# 4. Using Numpy module
# 5. Using a Python in-build sum() method


