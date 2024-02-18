
# Example: Using map, filter, and reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using map to square numbers
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Using filter to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Using reduce to sum numbers
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)
