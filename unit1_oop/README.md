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

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

Working through this assignment really clicked something into place for me. I finally got why people talk about OOP like it's a game-changer. I learned how inheritance lets you build on existing code instead of rewriting it constantly. The ChildClass inheriting from ParentClass felt natural, and seeing how super() lets you call parent methods without duplicating code was satisfying.

The namespace demonstration was the tricky part at first. I kept confusing where variables lived - class versus instance. But once I printed out __dict__ and saw exactly what each object held, it made sense. Same with shallow versus deep copying. Watching the shallow copy break when I modified nested data taught me that "copying" can be misleading if you're not careful.

Procedural programming gets you moving fast, but OOP is like building with LEGO instead of dumping sand. With procedures, you're managing tons of loose functions. With objects, related data and behavior live together.

The real benefit hit me when I realized maintainability means future-me won't hate current-me. If I need to change how skills work, I modify one place, not ten. Reusability cuts overhead because I'm not reinventing the wheel. When I build the next project, I can grab ChildClass and go. That's practical power.
