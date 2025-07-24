prompt = "Enter the topping you want us to add to your special pizza."
prompt += "\nPlease enter 'quit' to stop the program "

message = ""
while message != 'quit':
    message = input(prompt).lower()
    if message != 'quit':
        print(f"\nWe will add {message} topping to your pizza.")
