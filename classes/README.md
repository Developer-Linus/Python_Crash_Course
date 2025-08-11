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
  -  