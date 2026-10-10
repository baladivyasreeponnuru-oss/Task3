# Basic Rule-Based Chatbot

def get_reply(user_input):
    """Take the user's message and return the chatbot's reply."""
    message = user_input.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm PyBot, your simple chatbot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("=== CHATBOT ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        # Stop the loop when the user says bye
        if user_input.lower().strip() == "bye":
            break


# Run the chatbot
main()