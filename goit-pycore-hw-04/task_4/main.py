def parse_input(user_input: str) -> tuple:
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    """Add a new contact to the contacts dictionary."""
    if len(args) != 2:
        return "Invalid arguments. Please, provide name and phone number."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    """Update an existing contact in the contacts dictionary."""
    if len(args) != 2:
        return "Invalid arguments. Please, provide name and new phone number."

    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact does not exist."


def show_phone(args: list, contacts: dict) -> str:
    """Show the phone number for the contact."""
    if len(args) != 1:
        return "Invalid arguments. Please, provide name."

    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact does not exist."


def show_all_contacts(contacts: dict) -> str:
    """Show all contacts."""
    if not contacts:
        return "Contacts are empty."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """Main function to handle user input and commands."""

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in {"close", "exit"}:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")
        print()


if __name__ == "__main__":
    main()
