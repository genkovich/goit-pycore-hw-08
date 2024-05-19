from input_parser import parse_input
from address_book import AddressBook
import phone_base


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = phone_base.add_contact(args, book)
            print(result)
        elif command == "change":
            result = phone_base.change_contact(args, book)
            print(result)
        elif command == "phone":
            result = phone_base.show_phone(args, book)
            print(result)
        elif command == "all":
            phone_base.show_contacts(book)
        elif command == "add-birthday":
            result = phone_base.add_birthday(args, book)
            print(result)
        elif command == "show-birthday":
            result = phone_base.show_birthday(args, book)
            print(result)
        elif command == "birthdays":
            result = phone_base.birthdays(book)
            print(result)
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
