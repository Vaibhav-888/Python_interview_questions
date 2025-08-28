data = {"a": 50, "b": 5, "c": 20, "d": 9}
# 1. by using builtin function directly to sort dictionary
sorted_dict1 = dict(sorted(data.items(), key = lambda x: x[1]))
print(sorted_dict)

# 2. Optimised way to sort dictionary (using selection sort algorithm)
def sort_dictionary(data):
  """This function sorts the dictionary using selection sort algorithm in optimised way"""
  items = list(data.items())

  for i in range(len(items)):
    min_index = i
    for j in range(i + 1, len(items)):
      if items[j][1] < items[min_index][1]:
        min_index = j

    # swap the indexes to sort list of tuples in items
    items[i], items[min_index] = items[min_index], items[i]

  # convert the list of tuples i.e items into dictionary again
  # initialize with empty dictionary
  sorted_dict = {}
  for key, val in items:
    sorted_dict[key] = val

  return sorted_dict

print(sort_dictionary(data))
