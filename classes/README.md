# CLASSES
- OOP is one of the effective approaches for writing software.
- In OOP, you write `classes` that represent real-world things and situations, and you create `objects` based on these classes.
- When you write a class, you define the behaviour that a whole category will have. 
- Making an object from a class is called `instantiation`, and you work with `instances` from a class. 
- Knowing how to write classes helps improve logical thinking that is useful in solving any challenge I might encounter. 
## Creating and Using a Class
- You can model anything using classes.
- To create a class, you need to provide information (data) and behaviours (methods) of that class. For example, we can model the class dog for any dog. Let's say, for example, every dog has got a name and age. Also, every dog can sit or rollover. Information is name and age, while sit and roll over are behaviours. 
- After we have created a class, we use it to create individuals instances of the class.
### The `__init__()` method
- A function that is part of a class is a `method`. 
- Functions and methods are similar but difference occurs in the way they are called. 
- The `__init__()` method is a special method in Python that is run automatically when creating an instance of a class. 
- This method has two leading and two trailing underscores - helps in preventing your class methods names from conflicting Python default names. 
- `self` parameter is a must for methods and it must come before any other parameter. 
- When Python calls a method while creating an instance, it automatically passes `self` parameter to method calls. It is a reference to **instance itself**. It gives individual instance access to attributes and methods in a class.
- When creating an instance from a class, Python calls `__init__()` method. You need to pass in other paramters in this method except self because Python passes this automatically. 
- Why use `self`? Any variable with self prefix will make it available to the methods in class and can be accessed from the instance created. 
- Variables that are accessible through instances are called `attributes`.
### Making an Instance From a Class
- Think of a class as a set of instructions on how to create an instance.
#### Accessing Attributes
- use dot notation 
  ```
  instance.attribute_name
  ```

#### Calling Methods
- We use dot notation to access methods in an instance.
  ```
  instance.method()
  ```
## Working with Classes and Instances
- You can use classes to represent many real-world situations.
- Once you create a class, you mostly work with instances derived from that class.
- One of the things you can do is to modify attributes of the instance you are working with.
- You can update attributes directly or write methods that modify them in specific ways.
- To make a class more interesting, we can add an attribute that changes over time. 
### Setting a Default Value for an Attribute
- Every attribute in a class needs an initial value even if it is a 0 or empty string.
- It makes sense to set the initial value in `__init__()` method of a class.
> If you set the default value for an attribute, you don't pass it as a parameter in `__init__()` method.
## Modifying Attribute Values
- Achieved in 3 ways:
  ### 1. Modifying an Attribute Value Directly
  - Access the value of attribute directly through an instance and provide its value.
  - `my_car.odometer_reading = 23`
  ### 2. Modifying An Attribute's Value Through a Method
  - It is helpful to have methods that update attributes values.
  - You pass the new value to the method that updates internally.
  ### 3. Incrementing An Attribute's Value Through a Method
  - Sometimes, you would want to increment attribute's value by certain amount instead of providing a new value.
## Inheritance
- You don't always have to write a class from scratch.
- If the class you want to create is a special version of existing class, you use `inheritance` to create it.
- When one class inherits from another class, it automatically takes on all the attributes and methods of the first class.
- The original class is called `parent` class and the new class is called `child` class.
- The new class is free to define its own attributes and methods.
### The __init__() Method of a Child Class
- The task that Python has when creating an instance from a child class is to assign values to attributes in the parent class.To do this, the `__init__()` method in the child class needs help from the parent class.
- Parent and child must be on the same file or import it appropriately to make it accessible and should be above child.
- The name of the parent must be included in paranthesis after name of child class.
- `super()` is a special function in Python that tells it to make connections between parent and child class.
### Defining Attributes and Methods for Child Class
- Once you've child class, you can define its own new attributes and methods to differentiate it from the parent.
## Overriding Methods from Parent Class
- You can override method in the parent class that doesn't fit what you want to model with the child class.
- You achieve this by defining the method in child class with the same name as the method you want to override in the parent class. This way, Python will use what is in the child class and disregard what is in the parent class.
## Instances as Attributes
- When modelling something from real-world in code, you add more and more detail to class.
- Your number of attributes and methods grows increasing the length of your files. 
- When this happens, you recognize that part of one class can be written as a separate class.
- You break your large class into smaller classes that work together.
- If you want to call the method inside the attribute of the class, you use the class's attribute to access it.
## Modelling Real-World Objects
- 