# AC 2.3 - Git and GitHub Assessment
# Task 1: User input with validation

name = input("Enter your name: ").strip()

while not name:
    print("Name cannot be empty. Please try again.")
    name = input("Enter your name: ").strip()

print("Welcome,", name)