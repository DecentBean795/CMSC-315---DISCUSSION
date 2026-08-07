"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable - shared by all instances
    species = "Generic Object"
    
    def __init__(self, name, age):
        # Instance variables - unique to each instance
        self.name = name
        self.age = age
    
    def display_info(self):
        """Method that displays information about the object"""
        return f"{self.name} is a {self.species} and is {self.age} years old."
    
    def get_details(self):
        """Another method to demonstrate inheritance"""
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable specific to child class
    category = "Advanced Object"
    
    def __init__(self, name, age, skill):
        # Call parent class constructor
        super().__init__(name, age)
        # New instance variables
        self.skill = skill
        self.level = "Beginner"
    
    def display_info(self):
        """Override parent method"""
        parent_info = super().display_info()
        return f"{parent_info} Skill: {self.skill} (Level: {self.level})"
    
    def upgrade_skill(self):
        """New method in child class"""
        levels = ["Beginner", "Intermediate", "Advanced", "Expert"]
        current_index = levels.index(self.level)
        if current_index < len(levels) - 1:
            self.level = levels[current_index + 1]
            return f"Upgraded to {self.level}!"
        else:
            return "Already at Expert level!"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    
    # Create two objects of the child class
    obj1 = ChildClass("Alice", 25, "Python Programming")
    obj2 = ChildClass("Bob", 30, "Web Development")
    
    # Access class variable through the class itself
    print(f"\nClass variable accessed through ChildClass: {ChildClass.category}")
    print(f"Class variable accessed through ParentClass: {ParentClass.species}")
    
    # Access class variable through an object
    print(f"\nClass variable accessed through obj1: {obj1.category}")
    print(f"Class variable accessed through obj1 (from parent): {obj1.species}")
    
    # Add a new attribute to only obj1 after creation
    obj1.nickname = "Expert Coder"
    
    print("\n--- Object 1 Namespace (obj1.__dict__) ---")
    print(f"obj1.__dict__: {obj1.__dict__}")
    
    print("\n--- Object 2 Namespace (obj2.__dict__) ---")
    print(f"obj2.__dict__: {obj2.__dict__}")
    
    print("\n--- Class Namespace (ChildClass.__dict__ excerpt) ---")
    print(f"ChildClass class variables: category = '{ChildClass.category}'")
    print(f"ParentClass class variables: species = '{ParentClass.species}'")
    print(f"Methods in ChildClass: {[method for method in dir(ChildClass) if not method.startswith('_')]}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    
    # Create an object that contains nested mutable data
    original = ChildClass("Charlie", 28, "Data Science")
    # Add a nested mutable data structure (list of skills)
    original.skills_list = ["Python", "SQL", "Machine Learning"]
    original.projects = {"project1": ["data.csv", "model.pkl"]}
    
    # Create a shallow copy
    # Shallow copy copies the object but nested objects are referenced (not copied)
    shallow = copy(original)
    
    # Create a deep copy
    # Deep copy recursively copies the object and all nested objects
    deep = deepcopy(original)
    
    print("\n--- BEFORE Modifications ---")
    print(f"Original skills_list: {original.skills_list}")
    print(f"Shallow copy skills_list: {shallow.skills_list}")
    print(f"Deep copy skills_list: {deep.skills_list}")
    print(f"Original projects: {original.projects}")
    print(f"Shallow copy projects: {shallow.projects}")
    print(f"Deep copy projects: {deep.projects}")
    
    # Modify the original object's nested data
    original.skills_list.append("Statistics")
    original.projects["project1"].append("results.html")
    
    print("\n--- AFTER Modifying Original ---")
    print(f"Original skills_list: {original.skills_list}")
    print(f"Shallow copy skills_list: {shallow.skills_list}")
    print(f"Deep copy skills_list: {deep.skills_list}")
    print(f"Original projects: {original.projects}")
    print(f"Shallow copy projects: {shallow.projects}")
    print(f"Deep copy projects: {deep.projects}")
    
    print("\n--- Explanation ---")
    print("SHALLOW COPY:")
    print("  - The shallow copy was affected by changes to nested objects (list and dict)")
    print("  - This is because shallow copy copies references to nested objects, not the objects themselves")
    print("  - Both original and shallow copy point to the SAME nested list and dictionary")
    print("\nDEEP COPY:")
    print("  - The deep copy was NOT affected by changes to the original")
    print("  - Deep copy recursively copies all nested objects")
    print("  - The deep copy has its own independent nested list and dictionary")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    print("\n--- Parent Class Example ---")
    parent_obj = ParentClass("Generic", 5)
    print(f"Parent object info: {parent_obj.display_info()}")
    print(f"Parent object details: {parent_obj.get_details()}")

    # Create and test a child object
    print("\n--- Child Class Example ---")
    child_obj = ChildClass("David", 35, "Cloud Computing")
    print(f"Child object info: {child_obj.display_info()}")
    print(f"Child object details: {child_obj.get_details()}")
    print(f"Upgrade skill: {child_obj.upgrade_skill()}")
    print(f"Child object after upgrade: {child_obj.display_info()}")
    
    # Demonstrate inheritance by calling methods
    print("\n--- Demonstrating Inheritance ---")
    print(f"Child inherits get_details() from parent: {child_obj.get_details()}")
    print(f"Child overrides display_info(): {child_obj.display_info()}")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
