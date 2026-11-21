# Basic Chatbot
# CodeAlpha Python Internship Project

def chatbot():

    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)

    print("Chatbot: Hello! How can I help you?")
    print("Chatbot: Type 'bye' to exit the chat.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! Nice to meet you.")

        elif user_input == "how are you":
            print("Chatbot: I am fine, thank you!")

        elif user_input == "what is your name":
            print("Chatbot: I am a Python Chatbot.")

        elif user_input == "who created you":
            print("Chatbot: I was created using Python.")

        elif user_input == "what can you do":
            print("Chatbot: I can answer some basic questions.")

        elif user_input == "thank you":
            print("Chatbot: You're welcome!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
