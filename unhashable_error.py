"""
✅ Hashable Data Types (Immutable)
These can be used as dictionary keys or set elements:

Data Type	Hashable?	Notes
int	          ✅	     Immutable
float	      ✅	     Immutable
bool	      ✅	     Subclass of int
str	          ✅	     Immutable
tuple	      ✅	     Only if all elements inside are hashable
frozenset	  ✅	     Immutable version of set
bytes	      ✅	     Immutable sequence of bytes
NoneType	  ✅	     None is hashable
complex	      ✅	     Immutable complex numbers


for those datatypes are created and cannot be modified are hashable. 
e.g.: tuple, string, integer, float and boolean are hashable and immutable datatypes while we try to 
change an error occured as "tuple, set, str are does not support item assignment as traceback 
error"

While,

❌ Unhashable Data Types (Mutable)
These cannot be used as dictionary keys or set elements:

Data Type	Hashable?	Reason
list	        ❌	   Mutable
dict	        ❌	   Mutable
set	            ❌	   Mutable
bytearray	    ❌	   Mutable version of bytes
custom class	❌      (by default if __eq__ is overridden)	Must define __hash__ explicitly


🧠 Summary Rule

Immutable = Hashable ✅ (usually)
Mutable = Unhashable ❌ (usually)

But there are exceptions, especially with custom classes, 
which can be made hashable or unhashable depending on how you define __eq__ and __hash__.

"""

set = {1, 2, 3, 4, 5}
tuple = (1, 2, 3, 4, 5)
dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
list = [1, 2, 3, 4, 5]