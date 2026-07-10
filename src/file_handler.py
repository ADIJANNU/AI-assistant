import json
import os

RED   = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

CHAT_FILE = "data/chat_history.json"
PROFILE_FILE = "data/user_profile.json"

def save_chat(chat_history):
  with open(CHAT_FILE,"w") as f:
    json.dump(chat_history,f)
  print(f"{GREEN}✅ Chat saved!{RESET}")

def load_chat():
  if not os.path.exists(CHAT_FILE):
    return[]
  with open(CHAT_FILE,"r") as f:
    return json.load(f)
  
def save_profile(user):
  with open(PROFILE_FILE,"w") as f:
    json.dump(user,f)
  print(f"{GREEN}✅ Profile saved!{RESET}")

def load_profile():
  if not os.path.exists(PROFILE_FILE):
    return None
  try:
    with open(PROFILE_FILE, "r") as f:
      return json.load(f)
  except json.JSONDecodeError:
    print(f"{RED}⚠️ Profile file corrupted, starting fresh. {RESET}")
    return None

def reset_data():
  if os.path.exists(CHAT_FILE):
    os.remove(CHAT_FILE)
  if os.path.exists(PROFILE_FILE):
    os.remove(PROFILE_FILE)
  print(f"{GREEN}✅ Data cleared! New user can login.{RESET}")