#Assignment 1: Design Your Own Class
# Base class
class Wizard:
    def __init__(self, name, house, wand):
        self.name = name
        self.house = house
        self._wand = wand  # encapsulated attribute (protected)

    def cast_spell(self, spell_name):
        print(f"{self.name} casts {spell_name} with their {self._wand} wand!")

    def get_wand(self):
        return self._wand  # method to access protected attribute

    def __str__(self):
        return f"{self.name} from {self.house} house"

# Subclass
class Harry_Potter(Wizard):
    def __init__(self):
        # Use constructor from base class
        super().__init__(name="Harry Potter", house="Gryffindor", wand="Holly, 11\", Phoenix Feather")

    # Polymorphism: override the base method
    def cast_spell(self, spell_name):
        print(f"Harry bravely casts '{spell_name}' with his wand!")

    def use_invisibility_cloak(self):
        print("Harry uses the Invisibility Cloak to disappear!")

# Testing the classes
harry = Harry_Potter()

print(harry)  # Prints: Harry Potter from Gryffindor house
harry.cast_spell("Expelliarmus")  # Polymorphic behavior
harry.use_invisibility_cloak()  # Unique method
print("Harry's wand:", harry.get_wand())  # Accessing encapsulated data safely




#Activity 2: Polymorphism Challenge

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")


class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling down the path.")

# Create a list of vehicle objects
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Polymorphism in action
for v in vehicles:
    v.move()
