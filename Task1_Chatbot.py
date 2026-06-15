import random
print("🤖 Smart Student Assistant")
print("Type 'exit' to quit")
greetings = [
    "Hello! How can I help you?",
    "Hi there! Ask me anything.",
    "Welcome! What would you like to know?"
]
while True:
    user = input("\nYou: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    elif "name" in user:
        print("Bot: I am Smart Student Assistant.")

    elif "course" in user:
        print("Bot: AI & Data Science is a great field with many opportunities.")

    elif "python" in user:
        print("Bot: Python is one of the most popular programming languages.")

    elif "career" in user:
        print("Bot: Practice coding, build projects, and improve communication skills.")

    elif "motivate" in user:
        print("Bot: Success comes from consistency. Keep learning every day!")

    elif "bye" in user or user == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't have an answer for that yet.")
