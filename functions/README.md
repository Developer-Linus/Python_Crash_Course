# Functions

- Function is a named block of code designed to perform a specific task.
- Instead of repeating writing all the code, you just call the function.
- Functions help in writing, reading, fixing, and testing your program.

## Defining a Function

- Use `def` keyword to tell Python that you're defining a function.
- `function definition` tells Python function's name and the information that function needs to do its job. You pass the information in the parantheses.
- Even if you don't need any information, leave parantheses empty. Parantheses must be used.
- Function definition ends with a colon.
- Any indented block of code after function definition is its body.
- Use `docstring` to put a comment describing what the function does. They are enclosed in triple quotes. This docstring is what is used for documentation.
- A `function call` tells Python to execute code in function.

## Passing Information to a Function

- To pass information to a function, you specify them in the parantheses after functions. Each time you call a function, it expects you to input the values you specified in the parantheses.

## Arguments and Parameters

- `parameter` is done at function definition about information needed while `argument` is done at function calling. Parameter is piece of informatin a function expects to do its job. It is a variable. On the other hand, argument is the value you actually pass to a function as you're calling it.
- `parameter` is the variable that will hold the value you will pass during function calling. The value you pass as you're calling the function is an `argument.`

## Passing Arguments

- During function definition, you can pass sevaral parameters to the function. When you'll be calling, you will have to pass various arguments. There are several ways of doing this: `positional arguments` - you pass arguments in the same position as their respective parameters. `keyword arguments` - where each argument consists of variable name and its value; lists and dictionaries of values.

### Positional Arguments

- When you call a function, Python matches arguments with parameters in function definition.
- The easiest way to do this based on the order of the arguments provided. Values matched up this way are called `positional arguments.`
-
