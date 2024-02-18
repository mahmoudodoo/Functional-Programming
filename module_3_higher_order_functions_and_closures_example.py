
# Example of a higher-order function
def greet(func):
    greeting = func("Hi, I am a higher-order function")
    print(greeting)

def shout(message):
    return message.upper() + "!"

def whisper(message):
    return message.lower() + "..."

# Using the higher-order function
greet(shout)
greet(whisper)

# Example of a closure
def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function

my_func = outer_function('Hello')
my_func()
