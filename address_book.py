from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if (len(value) < 10) or (len(value) > 15):
            raise RecordValueError("Phone number must be between 10 and 15 digits")
        super().__init__(value)

    def __str__(self):
        return f"{self.value}"


class Birthday(Field):
    def __init__(self, value):
        try:
            value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise RecordValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        result = None
        for phone_value in self.phones:
            if phone_value.value == phone:
                result = phone_value
                break

        return result

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if not phone:
            raise RecordValueError("No such phone number")

        self.phones.remove(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_birthday(self, birthday):
        if self.birthday:
            raise RecordValueError("Birthday already exists")

        self.birthday = Birthday(birthday)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None

    def delete(self, name):
        del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.now()
        upcoming_birthdays = []
        for contact in self.data:
            birthday = self.data[contact].birthday.value
            tmp_birthday_date = birthday.replace(year=today.year)
            days_until_birthday = tmp_birthday_date - today
            if 7 >= days_until_birthday.days >= 0:
                if tmp_birthday_date.weekday() == 6:
                    tmp_birthday_date += timedelta(days=1)
                elif tmp_birthday_date.weekday() == 5:
                    tmp_birthday_date += timedelta(days=2)

                tmp_data = {
                    'name': self.data[contact].name.value,
                    'congratulation_date': tmp_birthday_date.strftime('%Y.%m.%d'),
                }
                upcoming_birthdays.append(tmp_data)

        return upcoming_birthdays


class RecordValueError(Exception):
    pass
