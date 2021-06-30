#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant
import json

with open("todo.json", "r") as todos:
  todo_list = json.load(todos)
  assistant = PersonalAssistant(todo_list)

#ADD CODE: open JSON file and pass data to PersonalAssistant class

done = False

while not done:
  user_command = input("\n\nHow can I help you? \n 1: Add a to-do\n 2: Remove a to-do\n 3: Get to-do list\n 4: Get Birthday \n 5: Get Contact\n 6: Exit\n Select a number: ")
  if user_command == "1":
    user_input = input("Item to add to to-do list: ")
    assistant.add_todo(user_input)
  elif user_command == "2":
    user_input = input("Item to remove from to-do list: ")
    assistant.remove_todo(user_input)
  elif user_command == "3":
    print("Your to-do list")
    print(assistant.get_todo())
  elif user_command == "4":
    user_input = input("Enter a name: ")
    print(assistant.get_birthday(user_input))
  elif user_command == "5":
    user_input = input("Enter a name: ")
    print(assistant.get_contact(user_input))
  elif user_command == "6":
    done = True
  else:
    print("Not a valid command.")

#ADD CODE: write data to JSON file
with open("todo.json", "w") as write_file:
  json.dump(assistant.get_todo(), write_file)

