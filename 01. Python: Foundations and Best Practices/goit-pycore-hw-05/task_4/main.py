from decorators import input_error


@input_error
def parse_input(user_input: str) -> tuple:
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    """Add a new contact to the contacts dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    """Update an existing contact in the contacts dictionary."""
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact does not exist."


@input_error
def show_phone(args: list, contacts: dict) -> str:
    """Show the phone number for the contact."""
    name = args[0]
    return contacts[name]


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
