"""
Yield Keyword and Generators in Python
    The yield keyword in Python is used to create generators. Generators are a special type of function that can pause their execution and resume later. Unlike traditional functions that return a single value, generators return an iterator object. This iterator yields values one at a time when used in a loop or with next().

Understanding Generators:

1. Function with yield: A generator function is defined like a regular function but uses the yield keyword to pause execution and return a value.
yield Keyword: The yield keyword acts as a checkpoint. When the generator encounters yield, it returns the value after yield and remembers its state (local variables).
2. Iterator Object: When you call a generator function, it doesn't execute completely. Instead, it returns an iterator object.
4. next() Method: You can use the next() method on the iterator to resume the generator's execution from where it left off, and get the next yielded value.
5. StopIteration: When the generator reaches the end (no more yield statements), calling next() raises a StopIteration exception.

Benefits of Generators over Traditional Functions:

- Memory Efficiency: Generators are memory-efficient when dealing with large datasets or infinite sequences. They yield values one at a time, avoiding creating a - - large data structure in memory all at once.
- Lazy Evaluation: Generators only calculate the values as needed, suitable for scenarios where you don't need all the results upfront."""


"""
Example: Square Numbers Generator
"""
def square_numbers(n):
    """Generates squares of numbers up to n."""
    for i in range(n + 1):
        yield i * i  # Pause execution and return the square

# Create a generator object
squares = square_numbers(5)

# Iterate over the generator using a for loop
for num in squares:
    print(num)

"""
Explanation:

    1. The square_numbers function is a generator function.
    2. The yield statement pauses execution after calculating i * i and returns the square.
    3. The function squares = square_numbers(5) creates a generator object, but doesn't execute the code yet.
    4. The for loop iterates over the generator object squares.
    5. In each iteration, next() is called internally to resume the generator, calculate the next square, and yield the value.

Key Points:

    - Generators are iterable (can be used in for loops) but not directly iterable themselves (you can't use them in functions expecting iterables like list() without converting them).
    - You can't directly call the generator function to get the result. It needs to be called to create an iterator object for usage.

By understanding generators and the yield keyword, you can write memory-efficient code for iterating over large datasets or creating infinite sequences in Python.
"""