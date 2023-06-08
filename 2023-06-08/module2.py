#!/usr/bin/python3
def hello():
    print("Hello from module.py")

print("This line always executes when module.py is imported.")

if __name__ == "__main__":
    print("This line executes only when module.py is run directly")
