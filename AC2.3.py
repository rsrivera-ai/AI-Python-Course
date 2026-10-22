# AC 2.3 - Git and GitHub Assessment
# Task 1: User input, validation and file storage

name = input("Enter your name: ").strip()

while not name:
    print("Name cannot be empty. Please try again.")
    name = input("Enter your name: ").strip()

print("Welcome,", name)

# Save the validated name to a text file
with open("user_names.txt", "a", encoding="utf-8") as file:
    file.write(name + "\n")

print("Your name has been saved successfully.")