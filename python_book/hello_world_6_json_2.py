from pathlib import Path
import json

path = Path("username.json")
content = path.read_text()
username = json.loads(content)

print(f"Welcome back, {username}!")

