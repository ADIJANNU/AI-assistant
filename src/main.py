import time
from error_handling import get_valid_int, get_valid_name
from file_handler import save_chat, load_chat, save_profile, load_profile, reset_data

# Colors
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
CYAN    = '\033[96m'
MAGENTA = '\033[95m'
WHITE   = '\033[97m'
RESET   = '\033[0m'

def get_user_input():
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{YELLOW}   Welcome to AI Assistant   {RESET}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")


    name = get_valid_name(f"{GREEN}Enter your name: {RESET}")
    age = get_valid_int(f"{GREEN}Enter your age: {RESET}")
    city = input(f"{GREEN}Enter your city: {RESET}").strip().title()
    goal = input(f"{GREEN}What do you want to learn: {RESET}").strip().lower()

    return  {
         "name"      : name,
         "age"       : age,
         "city"      : city,
         "goal"      : goal,
         "firstname" : name.split()[0],
    }

def show_menu():
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{YELLOW}   AI Assistant Menu{RESET}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{MAGENTA}1. View Profile{RESET}")
    print(f"{MAGENTA}2. Start Chat{RESET}")
    print(f"{MAGENTA}3. View Chat History{RESET}")
    print(f"{MAGENTA}4. Chat Stats{RESET}")
    print(f"{MAGENTA}5. Reset / Switch User{RESET}")
    print(f"{MAGENTA}6. Exit{RESET}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    return input(f"{YELLOW}Pick 1-6: {RESET}").strip()

    # Option 1 - View Profile
def view_profile(user):
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{GREEN}   Your Profile{RESET}")
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        for key, value in user.items():
            print(f"{CYAN}{key:<12}{RESET}: {WHITE}{value}{RESET}")
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

    # Option 2 - Start Chat
def start_chat(chat_history):
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
def view_history(chat_history):
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
def show_stats(chat_history):
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

class ChatSession:
     def __init__(self, messages = None):
          if messages is None:
             self.messages = []
          else:
             self.messages = messages
             

def run_app():

    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{YELLOW}   AI Assistant v1.0{RESET}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{GREEN}  Initializing...{RESET}")
    time.sleep(1)
    print(f"{GREEN}  Loading Profile...{RESET}")
    time.sleep(0.5)
    print(f"{GREEN}  Ready! {RESET}")
    time.sleep(0.5)


    user = load_profile()
    if user is None:
         user = get_user_input()
         save_profile(user)
    else:
         print(f"{GREEN}✅ Welcome back {user['firstname']}!{RESET}")

    chat_history = load_chat()

    while True:
        choice = show_menu()

        if choice == '1':
            view_profile(user)
        elif choice == '2':
            start_chat(chat_history)
            save_chat(chat_history)
        elif choice == '3':
            view_history(chat_history)
        elif choice == '4':
            show_stats(chat_history)
        elif choice == '5':
             reset_data()
             print(f"{YELLOW}Logged out!{RESET}")
             run_app()
             break
        
        elif choice == '6':
            print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            save_chat(chat_history)
            print(f"{YELLOW}   Goodbye {user['firstname']}! 👋{RESET}")
            print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Pick 1-5{RESET}")


run_app()
