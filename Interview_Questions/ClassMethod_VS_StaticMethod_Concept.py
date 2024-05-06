"""
Class Methods vs. Static Methods in Python

Both class methods and static methods are defined within Python classes, but they serve different purposes and have distinct characteristics:

Class Methods:

    - Definition: Decorated with @classmethod.
    - First Argument (cls): They receive the class itself as the first argument (cls). This allows them to access and potentially modify the class state (attributes and methods).
    - Use Cases:
        + Factory methods (creating objects of the class with specific configurations).
        + Utility methods that operate on the class itself (e.g., validating class attributes).

Static Methods:

    - Definition: Decorated with @staticmethod.
    - No Implicit Arguments: They don't receive any implicit arguments like self or cls. They behave like regular functions but are defined within a class for namespace organization or code reusability.
    - Use Cases:
        + Helper functions related to the class's functionality but not directly modifying the class state.
        + Mathematical or utility functions that don't rely on class attributes or methods.
"""

"""
Example:
"""
class Circle:
    PI = 3.14159  # Class attribute (shared by all instances)

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """Factory method: Create a Circle object from diameter."""
        radius = diameter / 2
        return cls(radius)  # Return a new Circle instance

    @staticmethod
    def calculate_area(radius):
        """Static method: Calculate the area of a circle."""
        return Circle.PI * radius**2

# Usage
circle1 = Circle(5)
circle2 = Circle.from_diameter(10)  # Using class method

area1 = circle1.calculate_area(circle1.radius)  # Accessing instance attribute
area2 = Circle.calculate_area(6)  # Using static method directly

print(f"Circle 1 area: {area1:.2f}")
print(f"Circle 2 area: {area2:.2f}")


"""
Explanation:

    1. The Circle class defines a PI class attribute and an __init__ method.
    2. The from_diameter method is a class method (@classmethod) that takes the class (cls) as the first argument. It creates a new Circle object using the provided diameter and returns it.
    3. The calculate_area method is a static method (@staticmethod). It doesn't receive any implicit arguments and simply calculates the area using the PI class attribute and the provided radius.
    4. We create two circles:
        - circle1 using the regular constructor.
        - circle2 using the from_diameter class method.
    5. We calculate the area for both circles:
        - area1 using the instance method (calculate_area) on circle1 (accessing its radius).
        - area2 using the static method directly (Circle.calculate_area) with a specific radius value.

Key Points:

    - Class methods are useful when you want to create objects of the class with specific configurations or perform operations on the class itself.
    - Static methods are helpful for utility functions related to the class's functionality but don't require access to the class state or object creation.
    - Choose the appropriate decorator (@classmethod or @staticmethod) based on whether your method needs to operate on the class itself or doesn't require any implicit arguments.
"""