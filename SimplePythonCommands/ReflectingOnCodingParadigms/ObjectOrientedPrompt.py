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

Q2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

Q3. How in particular did Object Oriented Programming assist in the solving of this problem?
"""