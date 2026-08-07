# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation Documentation

1. Parent Class

A `ParentClass` was created with a class variable named `species`. The class also contained two instance variables, `name` and `age`, which were initialized through the `__init__()` constructor. A `display_info()` method was created to return information about the object, and a second method named `get_details()` was created to return the name and age of the object.

2. Child Class and Inheritance

A `ChildClass` was created by inheriting from `ParentClass`. The child class added its own class variable named `category` and two additional instance variables, `skill` and `level`.

The `super().__init__()` method was used to initialize the inherited attributes from the parent class. The `display_info()` method was overridden so that the child object could display its additional information. The overridden method called `super().display_info()` and appended the skill and level values to the returned string, which allowed the parent output to be reused rather than rewritten.

A student-created extension was also added through the `upgrade_skill()` method. This method advanced the `level` attribute through an ordered list of proficiency values and returned a message describing the result. The inherited `get_details()` method was left unchanged so that inherited behavior could be demonstrated alongside overridden behavior.
 
 3. Class and Instance Namespaces

The `demonstrate_namespaces()` function created two objects from `ChildClass`. The class variables were accessed through both the class and an object, which showed that attribute lookup on an instance falls back to the class and then to the parent class.

A `nickname` attribute was then added to only the first object after it had been created. The `__dict__` attribute was used to display the individual namespaces of both objects, which showed that the added attribute appeared in one namespace and not the other. Information about the `ChildClass` namespace was also displayed to demonstrate the difference between a class namespace and an instance namespace, since the class variables `category` and `species` did not appear in either instance namespace.

4. Shallow and Deep Copying

The `demonstrate_copying()` function created a `ChildClass` object containing nested mutable data in its `skills_list` and `projects` attributes. A shallow copy was created using `copy()`, while a deep copy was created using `deepcopy()`.

The nested data in the original object was then modified in place. The results demonstrated that the shallow copy continued to share the nested mutable data with the original object, while the deep copy maintained an independent version of the nested data.

5. Main Function

The `main()` function created and tested both a `ParentClass` object and a `ChildClass` object. It called the inherited and overridden methods to demonstrate inheritance, and it called `upgrade_skill()` to show that the instance state of the child object had changed. The namespace and copying demonstration functions were also called from `main()`.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
Procedural programming gets you moving fast, but OOP is like building with LEGO instead of dumping sand. With procedures, you're managing tons of loose functions. With objects, related data and behavior live together.

