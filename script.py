import os

name = os.getenv("USER_NAME", "Unknown user")
print(f"Hello, {name}! This uses an environment variable.")
