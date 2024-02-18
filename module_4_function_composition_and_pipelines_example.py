
# Example of function composition
def add_five(x):
    return x + 5

def square(x):
    return x * x

# Composing the two functions
def square_then_add_five(x):
    return add_five(square(x))

print(square_then_add_five(5))  # Output: 30

# Example of a data processing pipeline
def pipeline(data, functions):
    for function in functions:
        data = function(data)
    return data

data = [1, 2, 3, 4, 5]
functions = [square, add_five]
print(pipeline(data, functions))  # Output: [6, 11, 18, 27, 38]
