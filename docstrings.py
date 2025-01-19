# In Python, you can document your functions using docstrings. A docstring is a 
# special string used to describe what a function does. It's placed immediately 
# after the function definition and is enclosed in triple quotes.


def greet(name="sangyog"):
    """
    This function greets the person passed in as a parameter.
    """
    print(f"Hello, {name}!")

print(greet.__doc__)  # Output: This function greets the person passed in as a parameter.
