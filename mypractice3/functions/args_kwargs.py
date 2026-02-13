# args_kwargs.py

# Using *args
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4))

# Using **kwargs
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Adina", age=18)
