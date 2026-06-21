
print("━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   Welcome to AI Assistant")
print("━━━━━━━━━━━━━━━━━━━━━━━━━")

user = {}

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: ").strip())
city = input("Enter your city name: ").strip().title()
goal = input("What do you want to learn: ").strip().lower()
firstname = name.split()[0]
next_year_age = age + 1


user = {
  "name": name,
  "age": age,
  "city": city,
  "goal": goal,
  "firstname": name.split()[0],
  "next_year": age + 1,
  "days_lived": age * 365
}

chat_history = []

while True:
    print("━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("   AI Assistant Menu")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("1. View Profile")
    print("2. Start Chat")
    print("3. View Chat History")
    print("4. Chat Stats")
    print("5. Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━")

    choice = input("Pick 1-5: ").strip()

 





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

