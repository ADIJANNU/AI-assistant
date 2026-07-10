import time
from error_handling import get_valid_int, get_valid_name
from file_handler import save_chat, load_chat, save_profile, load_profile, reset_data
from ai_client import get_ai_response

# Colors
RED, GREEN, YELLOW, BLUE, CYAN, MAGENTA, WHITE, RESET = '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[96m', '\033[95m', '\033[97m', '\033[0m'

class ChatSession:
     def __init__(self, messages = None):
          if messages is None:
             self.messages = []
          else:
             self.messages = messages
    
     def add_message(self, role, content):
          self.messages.append({
               "role": role,
               "content": content
          })

     def start_chat(self):
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{BLUE}   Chat Started{RESET}")
        print(f"{BLUE}   Type 'done' to stop{RESET}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        while True:
            message = input(f"{CYAN}You: {RESET}").strip()
            if message.lower() == 'done':
                break
            self.add_message("user", message)
            
            ai_reply = get_ai_response(message)
            self.add_message("assistant", ai_reply)
            print(f"{MAGENTA}Assistant: {ai_reply}{RESET}")


     def view_history(self):
        if len(self.messages) == 0:
            print(f"{RED}No messages yet!{RESET}")
        else:
            print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            print(f"{BLUE}   Chat History{RESET}")
            print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            for i, message in enumerate(self.messages):
                print(f"{CYAN}{i+1}.{RESET} {WHITE}{message['role'].title()}{RESET}: {message['content']}")
            print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

     def show_stats(self):
        if len(self.messages) == 0:
            print(f"{RED}No messages yet!{RESET}")
        else:
            total_words = 0
            longest = ''
            shortest = self.messages[0]['content']

            for message in self.messages:
                content = message['content']
                total_words += len(content.split())
                if len(content) > len(longest):
                    longest = content
                if len(content) < len(shortest):
                    shortest = content

            print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            print(f"{MAGENTA}   Chat Stats{RESET}")
            print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            print(f"{CYAN}Total messages{RESET} : {WHITE}{len(self.messages)}{RESET}")
            print(f"{CYAN}Total words   {RESET} : {WHITE}{total_words}{RESET}")
            print(f"{CYAN}Longest msg   {RESET} : {WHITE}{longest}{RESET}")
            print(f"{CYAN}Shortest msg  {RESET} : {WHITE}{shortest}{RESET}")
            print(f"{MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")


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

def view_profile(user):
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        print(f"{GREEN}   Your Profile{RESET}")
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
        for key, value in user.items():
            print(f"{CYAN}{key:<12}{RESET}: {WHITE}{value}{RESET}")
        print(f"{GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

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

    session = ChatSession(load_chat())

    while True:
        choice = show_menu()

        if choice == '1':
            view_profile(user)
        elif choice == '2':
            session.start_chat()
            save_chat(session.messages)
        elif choice == '3':
            session.view_history()
        elif choice == '4':
            session.show_stats()
        elif choice == '5':
             reset_data()
             print(f"{YELLOW}Logged out!{RESET}")
             run_app()
             break
        
        elif choice == '6':
            print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            save_chat(session.messages)
            print(f"{YELLOW}   Goodbye {user['firstname']}! 👋{RESET}")
            print(f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Pick 1-5{RESET}")


run_app()
