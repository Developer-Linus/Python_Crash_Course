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
- The easiest way to do this is to match them based on the order of the arguments provided. Values matched up this way are called `positional arguments.`
- Order matters in positional arguments. Follow the order you used in function definition as you will get errors or undesired results if they don't match.

### Keyword Arguments

- A `keyword argument` is a name-value pair that is passed when calling a function.
- You associate each name with a value.
- In this case, the order doesn't matter as every parameter declared in function definition has its exact value matched. Python knows where each value should go
- While using keyword arguments, ensure you use exact names of parameters used during function definition.

### Default Value

- When defining a function, you can give a `default value` to the parameters.
- During `function calling`, the argument you provide is used; otherwise, the default value is used.
- We use default values to ease the manner in which we call our functions depending on its frequent usage.
  > While using default values, it is recommended to place them as the last parameters in the function to adhere to the order of arguments while calling the functions.
  > The way you call your function doesn't matter so long as Python can correctly matches parameters in function definition and arguments in function calling.

### Avoiding Argument Errors

- With the help of Python traceback, you can easily idenfity the issue with your functions if you provide less or more arguments while calling your function.
- Always ensure you use descriptive variable names so that it becomes easier for you or any other person using your code.

## Return Values

- It is not always that functions displays its output.
- At times, it processes some inputs and return output.
- The output returned is called `return value`.
- The `return` statement takes a value inside the function and returns it to the line that called the function.
  > You need to create a variable to hold the value that a function returns.

### Making an Argument Optional

- Use default values to make an argument optional. This is useful for scenarios where users using the function want to provide extra information or not.

### Returning a Dictionary

- A function can return any type of value you want it to, including complicated data structures like lists and dictionaries.

## Using a Function with a While Loop

- 
