
# Example of working with a tuple (immutable data structure)
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# Attempting to modify the tuple will raise an error
# my_tuple[0] = 4  # Uncommenting this line will raise a TypeError

# Example of using frozenset (immutable set)
my_frozenset = frozenset([1, 2, 3, 4])
print("Frozenset:", my_frozenset)

# Frozensets are immutable
# my_frozenset.add(5)  # Uncommenting this line will raise an AttributeError
