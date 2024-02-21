class Car:
    [...]

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"
myCar = Car("Hyundai","Sonata")
print(myCar) #make: Hyundai, model: Sonata

#Below is short hand method  
__lt__(self,other) # <
__gt__(self,other) # >
__le__(self,other) # <=
__ge__(self,other) # >=
__eq__(self,other) # ==
__ne__(self,other) # !=


class Car:
    [...]

    def __eq__(self,other): # ==
        if self.make == other.make and self.model == other.model:
            return True
        else:
            return False

    def __ne__(self,other): # !=
        if self == other:
            return False
        else:
            return True
        
    def __str__(self):
        return f"make: {self.make}, model: {self.model}"

    def __repr__(self):
        return f"make: {self.make}, model: {self.model}"
    

car1 = Car("Hyundai","Sonata")
car2 = Car("Hyundai","Sonata")
car3 = Car("Honda","Accord")
print(car1 == car2) #True (self is car1, other is car2)
print(car1 == car3) #False (self is car1, other is car3)
print(car2 != car3) #True (self is car2, other is car3)

 
# This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
__repr__(self)

# This method returns the same value as __repr__(self).
__str__(self)

# Defines the '+' operator. If other is a Currency object, the currency values are added, and the result will be the unit of self. If other is an int or a float, it will be treated as a USD value.
__add__(self,other)

# This is the same as (calls) __add__(self,other).
__iadd__(self,other)

# This method is similar to __add__(self,other), but occurs when an int or float tries to add a Currency object. (Treat the int/float as having a USD value.)
__radd__(self,other)

# All __sub__(self,other) type functions are parallel to __add__(self,other) type functions.
__sub__(self,other)
__isub__(self,other)
__rsub__(self,other)
