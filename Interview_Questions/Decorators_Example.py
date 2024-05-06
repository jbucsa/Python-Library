""" 
Here's an example of a decorator in Python that demonstrates caching for performance optimization:
"""

import functools

def cache_decorator(func):
  """Decorator that caches function results based on arguments."""
  cache = {}

  @functools.wraps(func)  # Preserve function metadata (name, docstring)
  def wrapper(*args, **kwargs):
    cache_key = (args, tuple(kwargs.items()))  # Create a unique key for arguments
    if cache_key not in cache:
      cache[cache_key] = func(*args, **kwargs)
    return cache[cache_key]

  return wrapper

@cache_decorator
def fibonacci(n):
  """Recursive function to calculate the nth Fibonacci number."""
  if n < 2:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate Fibonacci numbers (cached results will be reused)
fib_10 = fibonacci(10)
fib_10_again = fibonacci(10)  # This will retrieve the cached value

print(f"Fibonacci of 10: {fib_10}")
print(f"Fibonacci of 10 (cached): {fib_10_again}")

""" 
Explanation:

    1. We import functools for the @functools.wraps decorator to preserve the wrapped function's metadata (name and docstring).
    2. The cache_decorator takes a function (func) as its argument.
    3. It creates an empty dictionary cache to store calculated results.
    4. The inner function (wrapper) receives arguments (*args and **kwargs) for the decorated function.
    5. It creates a unique cache_key based on the arguments and keyword arguments using a tuple.
    6. If the cache_key doesn't exist in the cache, it calls the wrapped function (func) with the arguments and stores the result in the cache under that key.
    7. Otherwise, it retrieves the cached result for the given arguments from the cache.
    8. Finally, it returns the result (either from the cache or the function call).
    9. The @cache_decorator syntax decorates the fibonacci function.
    10. The fibonacci function calculates Fibonacci numbers recursively.
    11. We call fibonacci(10) twice. The first call calculates the value and stores it in the cache.
    12. The second call with fibonacci(10_again) retrieves the cached value instead of recalculating it, demonstrating the performance benefit.

Key Points:

    - Decorators offer a clean and reusable way to modify function behavior.
    - Caching decorators can significantly improve performance for functions with expensive calculations or repeated calls with the same arguments.
    - The functools.wraps decorator helps preserve the metadata of the wrapped function, ensuring proper attribution and documentation.

By understanding decorators, you can write more modular, reusable, and efficient code in Python.
"""
