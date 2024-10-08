import os
from dotenv import load_dotenv

load_dotenv()

def greeting(name):
    greeting_prefix = os.getenv('GREETING_PREFIX', 'Hello')
    return f"{greeting_prefix}, {name}!"

if __name__ == "__main__":
    print(greeting("What"))
    print(greeting("Bro"))
    print(greeting("Are"))
    print(greeting("You"))
    print(greeting("Doing"))
    print(greeting("Something"))
    print(greeting("Good"))