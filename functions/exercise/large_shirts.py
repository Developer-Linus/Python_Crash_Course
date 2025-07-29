def make_shirts(shirt_size="Large", shirt_message="I love Python"):
    print("\nA T-shirt of size " + shirt_size.lower() +
          " with the message " + f"'{shirt_message}' has been made.")


make_shirts()
make_shirts(shirt_size="Medium")
make_shirts("Extra Large", "I love doing Python programming")
