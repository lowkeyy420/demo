import os
from dotenv import load_dotenv

load_dotenv()

def greeting(name):
    greeting_prefix = s.getenv('GREETING_PREFIX', 'Hello')
    return f"{greeting_prefix}, {name}!"

if __name__ == "__main__":
    print(greeting("World"))
    print(greeting("What"))
    print(greeting("???"))