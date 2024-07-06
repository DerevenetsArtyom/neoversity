from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        # Convert the birthday string to a datetime.date object
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Set the year to the current year to be able to compare with the current date
        birthday_this_year = birthday_date.replace(year=today.year)

        # If the birthday has passed this year, move it to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Get the number of days until the next birthday
        days_until_birthday = (birthday_this_year - today).days 

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append(
                {
                    "name": user["name"], 
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John", "birthday": "1985.01.23"},
    {"name": "Petro", "birthday": "1994.07.12"},
    {"name": "Monica", "birthday": "1989.07.06"},
    {"name": "Ivan", "birthday": "1996.07.13"},
    {"name": "Sara", "birthday": "1995.09.01"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("A list of greetings for the next week:")
for birthday in upcoming_birthdays:
    print(birthday)
