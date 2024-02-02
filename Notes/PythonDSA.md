### NOTES on DSA using Python
##### use this in conjunction with the hand written notes in Notability (add that to this repo once completed)


Arrays are a special type of list that can only hold one type of data and are fixed in size. In Python, arrays are not used as much as they are in other languages like C++ or Java. Instead, we use lists. Lists are more flexible and can hold different types of data. Lists are also dynamic, meaning they can change in size. Arrays are static, meaning they cannot change in size.

In Python, the term "arrays" is often used interchangeably with "lists," but there is a subtle difference between the two:

1. Lists:

Lists are a built-in data structure in Python, and they are very versatile.
Lists can store elements of different data types in a single container.
Lists are dynamic, meaning they can grow or shrink in size as needed.
Lists support various methods and operations like append, insert, remove, and more.
Lists can be created using square brackets [] or the list() constructor.

'''
my_list=[1,2,3,4]
'''

2. Arrays:

In Python, arrays are usually referred to as "arrays" when they are implemented using external libraries like NumPy or arrays from the array module.
Arrays typically store elements of the same data type.
Arrays have a fixed size when created and cannot easily change their size (although some libraries provide ways to resize arrays).
Arrays are optimized for numerical and scientific computing operations and are more memory-efficient than lists for large datasets.
Arrays are commonly used for tasks like matrix manipulation, statistical operations, and scientific computations.

'''
import numpy as np
my_array = np.array([1,2,3,4]) 
'''
