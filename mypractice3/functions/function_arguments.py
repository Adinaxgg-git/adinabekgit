# function_arguments.py

# Function with default argument
def greet_user(name="Guest"):
    print(f"Hello, {name}")

greet_user()
greet_user("Adina")

# Function with multiple positional arguments
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(5, 10)
