# Chatbot using if-elif-else
print("Hey! I'm your simple chatbot. Ask me anything (type 'bye' to exit).")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot: Hello! Nice to meet you.")
    elif user_input == "how are you":
        print("Chatbot: I'm doing great, thanks! What about you?")
    elif user_input == "what is your name":
        print("Chatbot: I'm just a chatbot built for fun!")
    elif user_input == "bye":
        print("Chatbot: Bye! See you later :)")
        break
    else:
        print("Chatbot: Hmm... I don't know how to answer that yet.")
