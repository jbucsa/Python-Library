""" 
In Python, decorators are a powerful and versatile syntactic feature that allows you to modify the behavior of functions without permanently altering their source code. They achieve this by wrapping a function with another function.

Here's a breakdown of how decorators work:

    1. Defining a Decorator Function:
        - A decorator is a regular Python function that takes another function as its argument.
        - This inner function (the function being decorated) is often referred to as the wrapped function.
    2. The @ Syntax:
        - The @ symbol is used before the decorator function name to indicate that it's being used as a decorator for the function following it.
        - When you call the decorated function, the decorator function is executed first, and it can optionally modify the behavior of the wrapped function or add new functionality.
    3. Returning the Wrapped Function (or a Modified Version):
        - The decorator function typically returns the wrapped function (unmodified) or a modified version of it. This allows the decorated function to retain its original functionality while potentially adding or altering its behavior.

Common Use Cases for Decorators:

    - Logging: Track function calls, arguments, and return values.
    - Authentication and Authorization: Restrict function access based on user permissions.
    - Error Handling: Add error handling logic to functions centrally.
    - Caching: Cache function results for performance optimization.
    - Timing: Measure the execution time of functions.
"""


""" 
Example: Logging Decorator
"""

def logging_decorator(func):
    """Decorator that logs function calls and arguments."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def add(x, y):
    """Simple function to add two numbers."""
    return x + y

# Call the decorated function
result = add(5, 3)

""" 
Explanation:

    1. We define a logging_decorator that takes a function (func) as its argument.
    2. The inner function (wrapper) receives arguments (*args and **kwargs) for the decorated function.
    3. It logs a message before calling the wrapped function (func).
    4. It captures the return value (result) from the wrapped function.
    5. It logs a message after the function call.
    6. Finally, it returns the result.
    7. We use the @logging_decorator syntax to decorate the add function.
    8. When we call add(5, 3), the logging_decorator is executed first, logging the call and arguments.
    9. The add function is then called, and the result is returned and logged by the decorator.

This is a basic example, but it demonstrates how decorators can be used to intercept function calls, modify their behavior, and potentially add functionalities like logging without directly changing the wrapped function's code.
"""