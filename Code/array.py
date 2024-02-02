# Arrays are a special type of list that can only hold one type of data and are fixed in size. In Python, arrays are not used as much as they are in other languages like C++ or Java. Instead, we use lists. Lists are more flexible and can hold different types of data. Lists are also dynamic, meaning they can change in size. Arrays are static, meaning they cannot change in size.

# 1. create arrays using lists

my_list = []
my_list_with_initial_values = [1,2,3,4,5]
my_list_with_initial_values_as_range = list(range(1,6))

# 2. access elements in an array

first_element = my_list_with_initial_values[0]
last_element = my_list_with_initial_values[-1]

# 3. modifying elements in an array

my_list_with_initial_values[0] = 10

