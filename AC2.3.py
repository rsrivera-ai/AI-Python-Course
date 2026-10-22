
# AC 2.3 - Git and GitHub Assessment
# Task 2: Refactoring code using reusable functions


def get_valid_name():
    """Ask for a name and reject empty input."""
    name = input("Enter your name: ").strip()

    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter your name: ").strip()

    return name


def save_name(name):
    """Append a validated user name to a text file."""
    with open("user_names.txt", "a", encoding="utf-8") as file:
        file.write(name + "\n")


def main():
    """Run the user greeting and file storage program."""
    name = get_valid_name()
    print("Welcome,", name)
    save_name(name)
    print("Your name has been saved successfully.")
    print("Temporary testing feature enabled.")

if __name__ == "__main__":
    main()
