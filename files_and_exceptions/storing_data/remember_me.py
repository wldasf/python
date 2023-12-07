from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        return info
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    info = {}
    username = input("What is your name? ")
    age = input("How old are you? ")
    origin = input("Where are you from? ")
    info['username_key'] = username
    info['age_key'] = age
    info['origin_key'] = origin
    contents = json.dumps(info)
    path.write_text(contents)
    return info

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    info = get_stored_username(path)
    if info:
        print(f"Your name is {info['username_key']} you are {info['age_key']} from {info['origin_key']}.")
        print(f"Welcome back, {info['username_key']}!")
    else:
        info = get_new_username(path)
        print(f"We'll remember you when you come back, {info['username_key']}!")

greet_user()