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
- In contrast, `while` loop runs as long as a certain condition is true.
- Most of the programs we interact with use while loops. For example, in a game, we need it to keep running as long as we want to play it. We need to be in control to tell it to quit when we no longer want to play. Programs lose fun part of it if they stop when we want to continue doing something or doesn't quit if we want to stop it.

## Letting the User Choose When to Quit

- You wrap the section of your program you want to keep running in `while` loop and provide the condition that must be true to keep the program running. Provide a way in which a user should stop the program from running.

## Using Flag

- Using single `while` loop is not efficient for complicated programs where more than one events can stop the program from running.
- For a program that runs as many conditions are true, you define a variable that determines wheter or not the whole program is active.
- This variable, called a `flag`, acts as a signal to the program.
- We can set our program to run as long as the flag is set to true. Then we define other sets of events that sets flag to false to stop the program from running.
- As a result, overall `while` statement only checks if `flag` is true or false to keep our program running.
- All the other tests that can set flag to false are neatly organized in the rest of the program.

## Using `break` to exit a loop

- To break a while loop and prevent remaining code from running, we use a `break` keyword. When the program reaches a break statement, it exits the loop immediately even if the condition is still true.
- `break` statement applies to any loop in Python, including for.

## Using Continue in a Loop

- We use `continue` statement for the loop to start over based on conditional test instead of breaking out entirely.

## Avoiding Infinite Loops

- Every `while` loop needs a way of stopping it so that it won't run forever.
- As a programmer, it is critical to test all the `while` loops you write to ensure it stops as needed. If you need a user to enter a given value, enter the value and verify if the program stops. If not, scrutinize your program and adjust the necessary sections to behave as expected.

# Using a While Loop with Lists and Dictionaries

- To keep track of records of pieces of information, we utilize lists and dictionaries in combination with `while` loops.
- A `for` loop is effective for looping through lists, but you cannot modify the lists as Python will have trouble tracking the items in a list.
- On the other hand, `while` loops allow you to modify lists as you work on them.
- Using `while` loop with lists and dictionaries enable us to collect, store, and organize lots of inputs for us to examine and report on later.

## Moving Items from One List to Another

- Assuming we've registered users awaiting verification before we move them to a list of verified users, how can we achieve this?
- One of the ways is to use a `while` loop where we extract users from unconfirmed list as we verify them and add to the list of confirmed users.

## Removing All Instances of Specific Values from a List

- `remove()` function only works if we have single instance of a value in list. What if we want to remove instances of repeated values from a list?
- The answer: Run `while` loop in the list until the repeated value you want to remove no longer exists.

## Filling a Dictionary with User Input

- You can prompt as much input as you want through each pass through a `while` loop.
- Take for example a scenario where you are taking a poll and you want to associate every response with its name.
