
print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   Welcome to AI Assistant")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")


name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: ").strip())
city = input("Enter your city name: ").strip().title()
goal = input("What do you want to learn: ").strip().lower()

firstname = name.split()[0]
next_year_age = age + 1
years_to_60 = 60 - age
goal_words = len(goal.split())

#  User profile section

print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   User Profile ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")

print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"Hello {firstname}!")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"{'Name': <10} : {name}")
print(f"{'Age': <10}  : {age}")
print(f"{'City': <10} : {city}")
print(f"{'Question' : <10} : {goal.title()}")

print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"{'Next year age' : <10} : {next_year_age}")
print(f"{'Years to 60': <10}  : {years_to_60}")
print(f"{'Goal words': <10}: {goal_words} ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")

# Chat History section

print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   Chat Session Started")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")

chat_history = []

msg1 = input("You: ").strip()
chat_history.append({"role": "user", "content": msg1})
msg2 = input("You: ").strip()
chat_history.append({"role": "user", "content": msg2})
msg3 = input("You: ").strip()
chat_history.append({"role": "user", "content": msg3})

print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   Chat History")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")

for message in chat_history:
  print(f"{message['role'].title()}: {message['content']}")


print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"Total messages: {len(chat_history)}")

