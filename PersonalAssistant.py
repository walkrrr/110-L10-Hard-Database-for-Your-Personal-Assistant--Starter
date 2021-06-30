class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {"Ann": "Marketing Coordinator", "Chelsea": "Software Developer", "Nichole": "Sales Representative",
    }
    self.todos = todos

  def get_contact(self, name):
      if name in self.contacts:
        return self.contacts[name]
      else:
        return "No contact with that name!"

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
        # Gets the todo_item index in list
      index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
        print("To-do is not in list!")

  def get_todo(self):
    return self.todos

  def get_birthday(self, name):
    if name == "Walkrrr":
      print("Birthday is 12/26!")
    elif name == "Missy": 
      print("Birthday is 05/03!")
    elif name == "DeVon":
      print("Birthday is 06/23!")
    else:
      print("Can't find a birthday for this person")

# This is the previous code from the Personal Assistant challenge in lesson 9.