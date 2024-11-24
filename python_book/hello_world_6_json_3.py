from pathlib import Path
import json
#
# path = Path("username.json")
#
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your username?> ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We will remember you, {username}!")


"""Refactoring - restructuring existing code without changing it's functionality"""

"""
def greet_user():
    "Greet the user by name"
    path = Path("username.json")

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your username?> ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you, {username}!")

greet_user()
"""

"""def get_stored_username(path):
    "Get stored username if available"
    if path.exists():
        ceontents = path.read_text()
        username = json.loads(ceontents)
        return username
    else:
        return None

def greet_user():
    "Greet user by name"
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your username?> ")#
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We will remember you, {username}!")


if __name__ == "__main__":
    greet_user()"""


def get_stored_username(path):
    "Get stored username if available"
    if path.exists():
        ceontents = path.read_text()
        username = json.loads(ceontents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username"""
    username = input("What is your username?> ")  #
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet user by name"""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We will remember you, {username}!")