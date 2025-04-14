"""
OOP Concepts Visualization in Python

Concepts covered:
- Class: Template for creating objects
- Object: Instance of a class
- Encapsulation: Protecting internal state of an object
- Inheritance: Reusing properties/methods from a parent class
- Polymorphism: Same method behaving differently based on object type
- Abstraction: Hiding complex implementation and showing only essential features
- Constructor (__init__ method): Special method used for initializing new objects

Workflow:
1. Define an abstract Animal class.
2. Create Dog and Cat classes inheriting from Animal.
3. Use Encapsulation by making sound a private attribute.
4. Demonstrate Polymorphism by overriding make_sound method.
5. Use constructors to initialize object properties during object creation.
6. Create objects and show interaction.
"""

class Animal:
    """
    Base class to represent any animal (shows abstraction).
    Attributes:
        name (str): Name of the animal.
        __sound (str): Private attribute to store sound (encapsulation).
    """
    def __init__(self, name, sound):
        """
        Constructor to initialize name and sound.
        __init__ is a special method that gets called automatically
        when an object is created from a class.
        Args:
            name (str): Name of the animal.
            sound (str): Sound made by the animal.
        """
        self.name = name
        self.__sound = sound  # private attribute (encapsulation)

    def make_sound(self):
        """
        Public method to make the animal sound.
        Demonstrates abstraction.
        """
        print(f"{self.name} says {self.__sound}")

    def _get_sound(self):
        """
        Protected method to access sound inside child classes.
        Supports encapsulation.
        """
        return self.__sound


class Dog(Animal):
    """
    Derived class from Animal (shows inheritance).
    Represents a Dog.
    """
    def __init__(self, name, breed):
        """
        Constructor for Dog.
        Calls the parent class (Animal) constructor using super().
        Args:
            name (str): Name of the dog.
            breed (str): Breed of the dog.
        """
        super().__init__(name, "Woof")  # Calls parent constructor
        self.breed = breed

    def make_sound(self):
        """
        Overridden method to customize dog sound.
        Demonstrates polymorphism.
        """
        print(f"{self.name} the {self.breed} barks: {self._get_sound()}")


class Cat(Animal):
    """
    Derived class from Animal (shows inheritance).
    Represents a Cat.
    """
    def __init__(self, name, color):
        """
        Constructor for Cat.
        Calls the parent class (Animal) constructor using super().
        Args:
            name (str): Name of the cat.
            color (str): Color of the cat.
        """
        super().__init__(name, "Meow")  # Calls parent constructor
        self.color = color

    def make_sound(self):
        """
        Overridden method to customize cat sound.
        Demonstrates polymorphism.
        """
        print(f"{self.name} ({self.color} cat) meows: {self._get_sound()}")


# --- Workflow demonstration ---

# Object creation (shows instantiation)
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Black")

# Calling methods (shows abstraction and polymorphism)
dog1.make_sound()    # Buddy the Golden Retriever barks: Woof
cat1.make_sound()    # Whiskers (Black cat) meows: Meow

# Encapsulation demonstration
# Private attributes are accessed through methods, not directly.
print(dog1._get_sound())  # Outputs: Woof

# Inheritance check
print(isinstance(dog1, Animal))  # True
print(isinstance(cat1, Animal))  # True

"""
Summary:
- Class Animal abstracts the concept of animals.
- Dog and Cat inherit properties but override behaviors (polymorphism).
- Sound attribute is encapsulated.
- Constructors (__init__) are used to initialize object properties.
- Object creation and method calling demonstrate how OOP ties everything together.
"""
