# Dictionary

- In Python, dictionary is a collection of `key-value` pairs.
- Defined using braces `{}`.
- Every key in dictionary has its associated value, and you can access the value associated with that key.
- The key's value can take a string, integer, list, dictionary, or any Python data type.

## Accessing values in a dictionary

- Give the name of dictionary and inside the square brackets, provide the name of the key. Python will return the value associated with that key.

## Adding New Key-Value Pairs

- Dictionaries are dynamic data structures and you can add key-value pairs at any time.
- To add a new key-value pair, provide the name of the dictionary and new key in square brackets along with the intended value.
- Python doesn't care about the order you used to add key-value pairs to the dictionary. It only cares about their connection between each key and its value.

## Starting with an Empty Dictionary

- At times, it is convenient or necessary to start with an empty dictionary and add key-value pairs at a later time.
- First, you define an empty dictionary with just braces.
- You can then add the key-value pairs.
- Commonly used in user-supplied data scenarios or when automatically generating key-value pairs.

## Modifying Values in a Dictionary

- To modify a dictionary's value, you give the name of the dictionary and provide the key in square brackets then give its new associated value.

## Removing Key-Value Pairs

- Use `del` statement to remove key-value pairs you no longer need.
- After `del`, you give name of the dictionary followed by its key in square brackets.
  > Deleted key-value pairs are permanently removed.

# A Dictionary of Similar Objects

- You can use a dictionary to store one kind of information for many objects.

# Looping Through a Dictionary

- Can be looked using its key or its value: You can loop through key-value pairs or through keys.
- `items()` method returns a list of key-value pairs for a dictionary.
- `keys()` method tells Python to pull all the keys from a dictionary.
- The default behavior for looping a dictionary is through `keys`. You can use the `keys()` method or leave it depending on the readability of your code.
- `keys()` function always return a list of keys present in the dictionary.

## Looping through a dictionary's key in order

- Keys are always returned with their associated value but not in any specific order.
- What we value most is how a key and its associated value are returned.
- We can specify the order using `sorted()` function by wrapping all the keys in it.

## Looping through all values in a dictionary

- If interested in the values in the dictionary, use `values()` method to get a list of all the values in a dictionary.
-
