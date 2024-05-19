from address_book import AddressBook, Record, RecordValueError


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RecordValueError as e:
            return str(e)
        except ValueError:
            return 'Not enough arguments'
        except KeyError as e:
            return str(e)
        except IndexError:
            return 'Please provide a name'

    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if record:
        return f"Contact {name} already exists."

    record = Record(name)
    if phone:
        record.add_phone(phone)
    book.add_record(record)
    return f"Contact {name} with phone {phone} was added."


@input_error
def change_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    if not record:
        return f"No such name in the phone book"

    record.add_phone(phone)
    return f"Contact {name} with phone {phone} was changed."


def show_contacts(book: AddressBook):
    for name, phone in book.items():
        print(f"{name}: {phone}")


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return f"No such name in the phone book"
    return f"{record}"


@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if not record:
        return f"No such name in the phone book"

    record.add_birthday(birthday)
    return f"Contact {name} added {birthday} birthday date."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return f"No such name in the phone book"

    if not record.birthday:
        return f"No birth date in the record for {name}"

    return f"{record.birthday.value}"


@input_error
def birthdays(book):
    return book.get_upcoming_birthdays()
