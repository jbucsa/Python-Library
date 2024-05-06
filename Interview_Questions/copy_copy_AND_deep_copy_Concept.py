"""
Shallow vs. Deep Copying with the copy Module in Python
    In Python, when dealing with compound objects (like lists, dictionaries, or custom classes) that contain references to other objects, creating copies becomes an important concept. The copy module offers two functions: copy.copy() and copy.deepcopy() to address different copying needs:

Shallow Copy:

    - Creates a new object of the same type.
    - Copies references to the original object's elements.
    - Changes made to the copied elements will affect the original elements as well, since they both refer to the same objects in memory.

Deep Copy:

    - Creates a new object of the same type.
    - Recursively copies all elements of the original object, creating entirely new objects in memory.
    - Changes made to the copied elements won't affect the original elements, as they are independent copies.

"""

"""
Using the copy Module:
"""
import copy

# Original data
data = [1, 2, [3, 4]]

# Shallow copy (references are copied)
shallow_copy = copy.copy(data)

# Modify a nested element in the shallow copy
shallow_copy[2][0] = 99

# Print both original and shallow copy
print("Original data:", data)
print("Shallow copy:", shallow_copy)
"""
Explanation:

    1. We import the copy module.
    2. We create a sample list data with a nested list.
    3. We create a shallow copy using copy.copy(). This creates a new list but copies references to the elements, including the nested list.
    4. We modify the first element in the nested list of the shallow copy (shallow_copy[2][0] = 99).
    5. We print both data and shallow_copy. You'll see that the modification in the shallow copy also affects the original data, as they both refer to the same nested list object.
"""



"""
Deep Copy:
"""
# Deep copy (entire structure is copied)
deep_copy = copy.deepcopy(data)

# Modify a nested element in the deep copy
deep_copy[2][0] = 55

# Print original, shallow copy, and deep copy
print("Original data:", data)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
"""
Explanation:

1. We create a deep copy using copy.deepcopy(). This recursively copies all elements, creating new objects in memory for the nested list as well.
2. We modify the first element in the nested list of the deep copy (deep_copy[2][0] = 55).
3. We print all three (original data, shallow copy, deep copy). You'll see that the modification in the deep copy is isolated, as it's a completely independent copy of the original data structure.
"""

"""
When to Use Shallow Copy:

- When you only need a new reference to the existing data structure and intend to modify its contents. This is faster than a deep copy.
- When dealing with simple data types (integers, strings, floats) that don't contain references to other objects.

When to Use Deep Copy:

- When you need a completely independent copy of the data structure to avoid unintended modifications to the original data.
- When working with complex data structures that contain nested objects or custom classes with references.
- When ensuring data integrity is crucial, and modifications to the copy shouldn't affect the original.

Remember:

- Deep copying is typically slower than shallow copying due to the recursive nature of copying all elements.
- The copy module also offers copy.copyreg for registering custom classes with specific copying behavior.


By understanding shallow and deep copying in Python, you can make informed decisions when working with compound data structures, ensuring data integrity and preventing unintended modifications when necessary.
"""