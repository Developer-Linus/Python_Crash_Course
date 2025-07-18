# User Input and While Loops

- Most programs are written to solve a user's problem.
- As a result, we need to collect some input from the user.
- In Python, we use `input()` function to collect information from the user.
- We need to make our programs running while some conditions are being met. Here is where we use `while` loop.
- The combination of `input()` function and `while` loop in Python make our programs more interactive among users.

## How the Input Function Works?

- Pause our program and wait for user to input some text. The received text is stored in a variable to make it convenient for us to use it.
- It takes only one argument: a _prompt_ or instructions we want the user to see for them to understand what they are expected to do.

## Writing Clear Prompts

- Clear, easy to understand prompt that tells the user the kind of information we are looking for.
- Add a space at the end of the prompt.
- Sometimes, you want to pass a long prompt to the input. Here, you store your prompt in a variable and use the variable as an argument in the input function.

## Using int() to Accept Numerical Input

- When we use `input()` function, Python interprets anything a user enters as a string.
- If we later want to use the input that the user entered to do some operations for an integer, then we have to convert it using `int()` function.
- `int()` function converts string representation of a number to its numerical representation.
- If I want to use numerical input to do calculations or comparisons, then I have to first convert it to numerical representation.

## Modulo Operator (%)

- Divides one number by another and returns the remainder.
- Used to determine if a number is odd or even.

# Introducing While Loop

- The `for` loop takes a collection of items and execute a block of code for each item in the collection.
- In contrast, `while` loop runs as long as certain condition is true.
