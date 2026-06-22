# Colors
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
CYAN    = '\033[96m'
MAGENTA = '\033[95m'
WHITE   = '\033[97m'
RESET   = '\033[0m'

print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
print(f"{YELLOW}   Welcome to AI Assistant{RESET}")
print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

user = {}

name = input(f"{GREEN}Enter your name: {RESET}").strip().title()
age = int(input(f"{GREEN}Enter your age: {RESET}").strip())
city = input(f"{GREEN}Enter your city name: {RESET}").strip().title()
goal = input(f"{GREEN}What do you want to learn: {RESET}").strip().lower()

user = {
    "name"      : name,
    "age"       : age,
    "city"      : city,
    "goal"      : goal,
    "firstname" : name.split()[0],
    "next_year" : age + 1,
    "days_lived": age * 365
}

chat_history = []

while True:
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{YELLOW}   AI Assistant Menu{RESET}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{WHITE}1. View Profile{RESET}")
    print(f"{WHITE}2. Start Chat{RESET}")
    print(f"{WHITE}3. View Chat History{RESET}")
    print(f"{WHITE}4. Chat Stats{RESET}")
    print(f"{WHITE}5. Exit{RESET}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    choice = input(f"{YELLOW}Pick 1-5: {RESET}").strip()

    # Option 1 - View Profile
    if choice == '1':
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{GREEN}   Your Profile{RESET}")
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        for key, value in user.items():
            print(f"{CYAN}{key:<12}{RESET}: {WHITE}{value}{RESET}")
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # Option 2 - Start Chat
    elif choice == '2':
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{BLUE}   Chat Started{RESET}")
        print(f"{BLUE}   Type 'done' to stop{RESET}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        while True:
            message = input(f"{CYAN}You: {RESET}").strip()
            if message.lower() == 'done':
                break
            chat_history.append({
                "role"   : "user",
                "content": message
            })
            print(f"{MAGENTA}Assistant: Got it! You said '{message}'{RESET}")

    # Option 3 - View Chat History
    elif choice == '3':
        if len(chat_history) == 0:
            print(f"{RED}No messages yet!{RESET}")
        else:
            print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            print(f"{BLUE}   Chat History{RESET}")
            print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            for i, message in enumerate(chat_history):
                print(f"{CYAN}{i+1}.{RESET} {WHITE}{message['role'].title()}{RESET}: {message['content']}")
            print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # Option 4 - Chat Stats
    elif choice == '4':
        if len(chat_history) == 0:
            print(f"{RED}No messages yet!{RESET}")
        else:
            total_words = 0
            longest = ''
            shortest = chat_history[0]['content']

            for message in chat_history:
                content = message['content']
                total_words += len(content.split())
                if len(content) > len(longest):
                    longest = content
                if len(content) < len(shortest):
                    shortest = content

            print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            print(f"{MAGENTA}   Chat Stats{RESET}")
            print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            print(f"{CYAN}Total messages{RESET} : {WHITE}{len(chat_history)}{RESET}")
            print(f"{CYAN}Total words   {RESET} : {WHITE}{total_words}{RESET}")
            print(f"{CYAN}Longest msg   {RESET} : {WHITE}{longest}{RESET}")
            print(f"{CYAN}Shortest msg  {RESET} : {WHITE}{shortest}{RESET}")
            print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # Option 5 - Exit
    elif choice == '5':
        print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{YELLOW}   Goodbye {user['firstname']}! 👋{RESET}")
        print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        break

    else:
        print(f"{RED}Invalid choice. Pick 1-5{RESET}")