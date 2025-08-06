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

- You can use a function with a `while` loop if there is some data collection from users.
- Ensure you handle well how users can quit the program.

## Passing a List

- Sometimes, I would find it useful to pass list to a function.
- When you pass a list to a function, the function will have access to the contents of the list.

## Modifying a List in a Function

- A function will modify the list if you pass a list as an argument.
- The modification that a function does to a list is permanent.

## Preventing a Function from Modifying a List

- At times you want to remain with the original list that you pass to the function.
- By default, the function modifies the list and it can leave it empty.
- To address this, you pass a copy of the list to the function.
  > ` function_name(list_name[:])`
- The slice notation `[:]` is used to create a copy of the list to pass to the funciton. 
## Passing an Arbitrary Number of Arguments
- At times, I don't know ahead of time the number of arguments will need.
- Fortunately, Python allows the calling of arbitrary arguments in calling statement. 
- We use an asterik `*` before a variable. Automatically, this tells Python to create a tuple that will pack its values receives and use them.
- Python packs everything, including even one argument passed into a tuple.
- You can then use `for` loop to tailor the function to your needs.
## Mixing Positional and Arbitrary Arguments
- If I want to use different arguments in my function, I have to place arbitrary parameters at the end during function definition.
- This is because Python matches positional and keyword arguments before collecting other arguments in the final parameter.
## Using Arbitrary Keyword Arguments
- This one is used if you don't know ahead of time the number of key-value pairs that will be passed in the calling statement.
- We use double asteriks (**) to tell Python to create an empty dictionary for holding the key-value pairs that a user will provide. 
> Arbitrary arguments use single asterik while arbitrary keyword arguments use double asterik. The variables passed as arguments for arbitrary arguments are stored in a tuple unlike a dictionary that stores key-value pairs of the arbitrary keyword arguments.
## Storing Your Functions in Modules
- Advantage of functions: separate blocks of code from your main program.
- It will be much easier to follow my program given that I have descriptive functions names. 
- I can go a step further by creating my functions in a file called `module` and later importing it to my main program. 
- An `import` statement tells Python to make code in a module available for use in the current program file.
- Advantages of storing functions in a separate file:
  > allows you to hide the details code of your program and focus on higher-level logic.
  > allows you to reuse functions in many different parts of your program.
  > I can share those separate functions files with other programmers without sharing my main program.
- When I know how to import functions, I can easily use other libraries of functions other programmers have written. 
- The ways of importing a module include:
### 1. Importing an Entire Module
- First, you need to have a `module`, file ending in *.py*, that has your function.
- You now import that module in your current program file you want to use it.
- The `import` statement tells Python to copy all functions in a module and make it available in the current program.
  ```
  import module_name
  ```
- using this approach makes all functions in the module available. To use specific function, you write name of the module followed by dot(.) then name of the function as:
  ```
  module_name.function_name()
  ```
### 2. Importing Specific Functions
- General syntax for this approach is:
  ```
  from module_name import function_name
  ```
- From a module, you can import as many functions as you want separated by a comma.
  ```
  from module_name import function1, function2
  ```
- Using this approach, you don't use dot notation to access and use your function because you've explicitly specified in the `import` statement.
### 3. Using `as` to Give a Function an Alias
- If your function name conflicts with an existing name in your program or your function's name is too long, you use a short, unique `alias` that is an alternate name similar to nickame to the function.
- General syntax:
  ```
  from module_name import function_name as fn
  ```
- This approach renames function name, function_name, to fn. So when we will be calling the function, we will use fn and not function_name.
### 4. Using `as` to Give a Module an Alias
- You can also give a module an alias.
- This is a short name that will make calling functions quicker.
- General syntax:
  ```
  import module_name as md
  ```
