# Python doesn't concatenate an integer and a string. For concatenation to work, we have to convert all non-string to string using str() function
age = 29
message = "Happy " + str(age) + "rd birthday!"
print(message)