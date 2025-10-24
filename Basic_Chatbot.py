def chatbot():
    print("🤖 Simple Chatbot (type 'bye' to exit)")
    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("Bot: Hi there!")
        elif "how are you" in user:
            print("Bot: I'm fine, thanks! How about you?")
        elif "bye" in user:
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I didn’t understand that.")

if __name__ == "__main__":
    chatbot()
