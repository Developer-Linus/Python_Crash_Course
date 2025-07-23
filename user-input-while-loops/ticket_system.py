active = True
message_limit = 5
message_count = 0


prompt = "\nWelcome to the support center. Please specify the issue you are encountering."
prompt += "\nType 'exit' if you want to close the chat or 'resolved' if the issue has been addressed. "
while active:
    message = input(prompt).lower()
    if message == 'exit':
        print('\nYou have exited the support session. Goodbye!')
        active = False
    elif message == 'resolved':
        print("\nWe are glad the issue was resolved. Thank you for contacting the support.")
        active = False
    elif message == "":
        print("Please type something so that we can assist you.")
    else:
        print(f"Thank you for your message: {message.capitalize()}")
        print("We will get back to you shortly.")

        message_count += 1

        if message_count >= message_limit:
            print("You have exceeded maximum support center messages for this chat.")
            print("Our support will review your messages shortly and get back to you.")
            active = False
