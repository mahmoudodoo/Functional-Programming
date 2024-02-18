
# Example: Imperative vs Functional Style

# Imperative style
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print("Imperative:", squared_numbers)

# Functional style
squared_numbers_func = list(map(lambda x: x**2, numbers))
print("Functional:", squared_numbers_func)
