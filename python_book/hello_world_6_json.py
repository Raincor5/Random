from pathlib import Path
import json

username = input("What is your username? ")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember you, {username}!")
