"""
The enumerate function in Python is a built-in function used for iterating over iterables (like lists, tuples, or strings) and keeping track of the index (position) of each element. It returns an enumerate object, which is an iterator that yields tuples containing two elements:

    1. Index: The current index (position) of the element within the iterable. This starts from 0 by default.
    2. Value: The element itself from the iterable.
"""

"""
Using enumerate in a for loop:
"""

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

"""
OUTPUT:
    Index: 0, Fruit: apple
    Index: 1, Fruit: banana
    Index: 2, Fruit: cherry
"""

"""
As you can see, the enumerate function allows you to access both the index and the element simultaneously within a for loop, making it convenient for scenarios where you need to process both the position and the value of each item in an iterable.

Here are some additional points about enumerate:

    - Starting Index: You can optionally specify a starting index for the counter by passing a second argument to enumerate. For example, enumerate(fruits, 1) would start the index at 1.
    - Unpacking in Loops: You can use unpacking in for loops to directly access the index and value:
"""

for i, fruit in enumerate(fruits):
    print(f"{i+1}. {fruit}")  # Start index from 1 for a numbered list

"""
    - Iterables: enumerate works with various iterables, not just lists. You can use it with strings, tuples, dictionaries (keys only), and other custom iterables.

By understanding enumerate, you can write concise and efficient for loops in Python where you need to work with both the index and the value of elements within an iterable.
"""