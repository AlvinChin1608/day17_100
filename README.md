# day17_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner stage and later on intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------------------------------------------------

# Introduction to Python Classes

## What is a Class?

A **class** in Python is a blueprint for creating objects. Objects represent real-world entities and have attributes (data) and methods (functions) that define their behavior. Classes allow you to bundle data and functionality together.

## Basic Terminology

- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.
- **Attribute**: A variable that belongs to an object or class.
- **Method**: A function that belongs to an object or class.

## Defining a Class

You define a class using the `class` keyword followed by the class name and a colon. The class name should follow the PascalCase naming convention.

```python
class MyClass:
    # Class attribute
    class_attribute = "I am a class attribute"
    
    # Initializer / Instance attributes
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        
    # Method
    def my_method(self):
        print(f"Attribute1: {self.attribute1}, Attribute2: {self.attribute2}")
```


**Creating an Object**
You create an object by calling the class as if it were a function.

```python
my_object = MyClass("Value1", "Value2")
```

**Accessing Attributes and Methods**
You can access attributes and methods using the dot (.) notation.

```python
print(my_object.attribute1)  # Output: Value1
my_object.my_method()        # Output: Attribute1: Value1, Attribute2: Value2
```

**Example**

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Method to get dog's age in dog years
    def get_age_in_dog_years(self):
        return self.age * 7

Create instances of Dog
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

Access attributes and methods
print(dog1.name)               # Output: Buddy
print(dog2.age)                # Output: 3
print(dog1.bark())             # Output: Buddy says woof!
print(dog2.get_age_in_dog_years())  # Output: 21
```

**The __init__ Method**
The __init__ method is a special method called a constructor. It is automatically called when an object is created from a class and allows the class to initialize the object's attributes.

**The self Keyword**
The self keyword represents the instance of the class. It is used to access variables and methods associated with the current object.

**Class Attributes vs. Instance Attributes**


**Class Attributes:** Shared across all instances of a class.

**Instance Attributes:** Unique to each instance.
```python
class Car:
    # Class attribute
    wheels = 4
    
    def __init__(self, color, model):
        # Instance attributes
        self.color = color
        self.model = model

# Create instances
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
print(car1.color)   # Output: Red
print(car2.color)   # Output: Blue
```



