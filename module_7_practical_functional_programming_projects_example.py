
# Example: A simple data analysis pipeline using functional programming concepts

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def filter_data(data, condition):
    return [item for item in data if condition(item)]

def transform_data(data, transformation):
    return [transformation(item) for item in data]

def write_data(data, file_path):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

# Example usage
file_path = 'data.txt'
filtered_file_path = 'filtered_data.txt'
data = read_data(file_path)
filtered_data = filter_data(data, lambda x: 'Functional' in x)
transformed_data = transform_data(filtered_data, lambda x: x.upper())
write_data(transformed_data, filtered_file_path)
