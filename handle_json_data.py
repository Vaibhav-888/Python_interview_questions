# find the common hobbies from the given json data
# methods like permutations and combinations
# this solution is dynamic without taking any hardcoded variables

"""
The primary uses of the json module include:
Serialization (Encoding):
Converting Python objects (like dictionaries, lists, strings, numbers, booleans, and None) into JSON formatted strings.
json.dumps(): Serializes a Python object into a JSON formatted string.
json.dump(): Serializes a Python object and writes it to a file-like object (e.g., a file).

Deserialization (Decoding):
Converting JSON formatted strings or files back into Python objects.
json.loads(): Deserializes a JSON formatted string into a Python object.
json.load(): Deserializes JSON data from a file-like object into a Python object.

Common applications of the json module:
Web APIs: Exchanging data between clients and servers, where many web services return data in JSON format.
Configuration Files: Storing application settings and configurations in a human-readable and easily parsable format.
Data Storage: Storing structured data in files for small to medium-sized applications.
Data Analysis: Loading JSON data into Python for analysis using libraries like Pandas.
Interoperability: Facilitating data exchange between different programming languages and systems that support JSON.

"""

import json
from itertools import combinations

data = """[
    {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]},
    {"name": "Bob", "age": 25, "hobbies": ["gaming", "coding"]},
    {"name": "Charlie", "age": 35, "hobbies": ["cooking", "hiking"]}
]"""



users = json.loads(data)
# print(users)

for user1, user2 in combinations(users, 2):
    common = set(user1["hobbies"]) & set(user2["hobbies"])
    if common:
        hobby_str = " ".join(common)
        print(f"{user1["name"]} and {user2["name"]} have common hobby is {hobby_str}.")