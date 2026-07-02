RED   = '\033[91m'
RESET = '\033[0m'

def get_valid_int(prompt):
  while True:
    try:
      return int(input(prompt).strip())
    except ValueError:
      print(f"{RED}❌ Please enter a number!{RESET}")

def get_valid_name(prompt):
  while True:
    name = input(prompt).strip().title()
    if name == "":
       print(f"{RED}❌ Name cannot be empty!{RESET}")
    elif not name.replace(" ", "").isalpha():
       print(f"{RED}❌ Name should only contain letters!{RESET}")
    else:
        return name