"""" 
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.
    First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
    Define a repair() method that will update the condition of the podracer to "repaired".
    Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
    Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
"""

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"


"""

Make sure to answer the following prompts about your coding experience:

Q1. How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    A. This solution demonstrates two pillars of Object-Oriented Programming (OOP):
    
    Encapsulation: Each class encapsulates its own data (attributes) and behaviors (methods). Attributes like max_speed, condition, and price are encapsulated within their respective classes (Podracer, AnakinsPod, SebulbasPod), and methods like repair, boost, and flame_jet provide controlled access to manipulate these attributes. Encapsulation helps in managing complexity by hiding internal implementation details and exposing only necessary interfaces to interact with objects.
    
    Inheritance: AnakinsPod and SebulbasPod classes inherit from the base class Podracer. This inheritance relationship allows them to inherit attributes and methods from Podracer and extend or modify them as needed. For example, AnakinsPod inherits the repair method from Podracer and adds a new method boost, while SebulbasPod inherits the repair method and adds a new method flame_jet. Inheritance promotes code reusability and supports hierarchical classification, where specialized classes can be created from a more general superclass.

    
Q2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    A. Using Object-Oriented Programming (OOP) for this problem offers several benefits:
    
    Modularity: OOP allows breaking down the problem into smaller, manageable components (classes), each representing a distinct entity (Podracer, AnakinsPod, SebulbasPod). This promotes independent development, testing, and maintenance of these components.
    
    Abstraction: OOP promotes abstraction by focusing on the essential characteristics of objects while hiding unnecessary details. The classes abstract away the complexity of managing podracer inventory by providing a clear interface (attributes and methods) for interacting with the objects.
    
    Flexibility and Extensibility: OOP facilitates easy extension and modification of the system. New types of podracer classes can be added in the future by creating new subclasses or modifying existing ones without impacting the overall system architecture. This enhances the system's adaptability to changing requirements.

    
Q3. How in particular did Object Oriented Programming assist in the solving of this problem?
    A. Overall, Object-Oriented Programming assists in solving this problem by providing a structured and modular approach to designing and implementing the system, promoting code reuse, maintainability, and scalability.

"""