
# Example of a pure function
def add(a, b):
    return a + b

# Example of using immutable data structures
def square_list_immutable(lst):
    return [x**2 for x in lst]

# Using the pure functions
print(add(3, 4))  # Output: 7
original_list = [1, 2, 3, 4]
new_list = square_list_immutable(original_list)
print(new_list)  # Output: [1, 4, 9, 16]
