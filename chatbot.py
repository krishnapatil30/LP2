from datetime import datetime

def chatbot():
    print("Hello! I am your chatbot.")

    name = input("Enter your name: ")
    print("Nice to meet you,", name)

    while True:
        print("\nHow can I help you?")
        print("1. Tell time")
        print("2. Tell date")
        print("3. Simple questions")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current Time:", datetime.now().strftime("%H:%M:%S"))

        elif choice == "2":
            print("Today's Date:", datetime.now().strftime("%d-%m-%Y"))

        elif choice == "3":
            question = input("Ask me something: ").lower()

            if "hello" in question or "hi" in question:
                print("Hello there!")

            elif "how are you" in question:
                print("I'm just code, but I'm doing great!")

            elif "your name" in question:
                print("I am a simple chatbot.")

            else:
                print("Sorry, I don't understand that.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

chatbot()