# Lists

- **List** is a collection of items in a particular order.
- Good idea to make the name of a list _plural_.
- Square brackets ([]) indicate list. Individual items in a list are separated by a comma.

# Accessing Elements in a List

- Lists are ordered collections, and to access an element in a list, you tell Python the position, or _index_ of the desired element.
- To access an element, you write the name of the list followed by its index enclosed in square brackets.
  > Index positions start at 0, not 1.
- To access the last item in a list, use -1. This tells Python to always return last element in a list.
  > You can use individual values from a list the same way you can with others. You can concatenate with other parts of a string.

# Changing, Adding, and Removing Elements

- Mostly, we will handle dynamic lists.
- For instance, in gaming, most aspects will keep on increasing and decreasing to make it more interesting for the players.

# Modifying Elements

- Its syntax is similar to the one of accessing elements in a list. You provide the name of a list followed by index and finally the new value you want to insert.

# Adding Items to List

## Appending Elements to the End of The List

- To add element to the end of a list, we use `append()` function. In the parantheses, we put the value of the element.
- `append()` function makes list dynamic. You can start with an empty list and keep on appending as the list evolves.

## Inserting Elements into a List

- Use `insert()` method to insert an element at any position in the list.
- Achieved by specifying the index and value of the new item.
- It creates an empty space in the specified index and push other elements respectively before inserting the new element.

## Removing Elements from a List

### 1. using del statement

- Used to delete an element if you know its position.
- Once you execute the statement, you will not have access to it.

### 2. using pop() method

- Used if you want to have access of removed element for other purposes.
- Using `pop()` without giving any index removes the last item in a list.
- Useful if you want to get the most recent or last item added to the list.

### 3. Popping Items from any Position in a List

- You include the index in the parantheses of `pop()` method.
  > It can be confusing to decide when to use `pop()` or `del`. The rule is that if you want to remove an item and use it, use `pop()`, otherwise, use `del`.

### 4. Removing an Item by Value

- Use `remove()` method to remove an element if you don't know the index but know its value.
- Remove returns the value of the deleted item.

# Organizing a List

- At times, it is challenging to control how a list will appear.
- This is because you could not be the one entering items in a list.
- The issue could be that you want a list to be put in a particular.
- Python provides us with various methods of organizing a list based on a situation.

## 1. Sorting a List Permanently with sort() Method

- Changes the order of items in a list permanetly. You can never revert to the original list.
- If you want the items to be ordered in reverse order, pass in the argument `revert=True` to the sort method.

## 2. Sorting a List Temporarily with sorted() Function

- Useful if I want to maintain the original order but sort it in a particular order.
- Allows you to display items in a list in a particular order without affecting the actual order of a list.
- You can also pass in the argument `reverse=True` to the sorted() function to reverse the order.

> All the values should be in lowercase to sort them in alphabetical order.

## 3. Printing a List in Reverse Order

- You use `reverse()` method to reverse the original order of list. It arranges items in a list in reverse chronological order.
- This doesn't sort items in a list. It just reverses the list.
- Changes the order of the list permanently. To revert to original order, apply reverse() method also.

## 4. Finding Length of a list

-We use `len()` function to find the lenght of a list.

- ## It gives the number of items in a list.

# Working with Lists

- Here, we'll discuss about about `looping` in lists to perform an action or set of actions on a list regardless of its length. As a result, we will be able to work more efficiently.

## Looping Through an entire List

- Python's `for` loop is great for performing same action on every item in a list.
- Assume we have a list of items in a list. If we want to print each item, we will have to write line(s) of code for each item. If the items in the list changes, we have to change our code. `For` loop solves the problem of writing long pieces of code and changing lines of code every time item(s) in a list changes.
- `Looping` is one of the ways a computer automates repetitive tasks.
- Computers don't move to next line of code until looping process ends.
- Choose a meaningful name for a variable that will hold each item in a list.
- Any indented piece of code after `for` loop statement is executed before next loop. You can write as many of them as possible.
- After a for loop, you might want your program to continue running or write other lines of code. You can write something wrapping up what has happened for `for` loop.

# Avoiding Indentation Errors

- Indentation in Python shows that the lines of code is connected to the line above it.
- In writing programs, we might find ourselves forgetting to indent or indenting what is not suppose to be indented.

# Making Numerical Lists

- we can use `range()` function.
- we convert range values into a list using `list()` function. We pass range values as argument to the list function.

# Working with Part of a List

- We can work with specific elements in a list. In Python, this is called a `slice`.

## Slicing a List

- You specify the first and second indices of the items you want for a slice. The program stops before the second index and returns the elements.
- You can create a subset of a list by specifying the first and second indices.
- You can loop through a list slice using `for` loop.

## Copying a List

- You might want a copy of the list you have and modify later to add other elements. This is where copying existing list is key.
- We can create a slice of the full list by not providing the first and second indices.
  `list[:]`
- 
