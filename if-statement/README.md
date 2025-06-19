# If Statement

- Programming entails examining a set of conditions and performing actions based on a particular condition.
- Python's `if` statement evaluates the current state of a program and respond appropriately to that state.

## Conditional Tests

- At the core of every `if statement`, there is an expression that evaluates to either `True` or `False` and it is called a `conditional test`.
- Python evaluates `if` statement. If `True` it executes the code block under `if` block. If `False`, it ignores the code block under if statement.

### Checking for Equality

- Most conditional tests compare the value of a variable to a specific value of interest.
- `==` is the `equality operator` for comparing values.

### Ignoring Case When Checking for Equality

- Testing for equality is case sensitive.
- Values with different capitalization are considered unequal.

### Checking for Inequality

- We use an exclamation mark and an equal sign (`!=`).

## Numerical Comparisons

- This is straightforward. You can use any equality applicable to mathematical expressions to achieve your desired comparison.

## Checking Multiple Conditions

- At times, you want to check two conditions at the same time. Here, you use `and` and `or` keywords to achieve this.

### Using `and` to check multiple conditions

- Checking it two conditions are both `True` simultaneously. If both evaluates to `True`, the block of code within if statement is executed. If one or both evaluates to `False`, the program ignores the code block under if statement.

### Using `or` to check multiple conditions

- It passes when either or both of tests pass. It fails if both tests fail.

## Checking Whether a Value is in a List

- Use the keyword `in`.

## Checking Whether a Value is not in a List

- Use the keyword `not in`.
