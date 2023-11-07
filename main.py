from datetime import date, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    new_users = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    today = date.today()
    year = today.year
    next_week = today + timedelta(days=7)

    for user in users:
        name = user['name']
        birthday_date = user['birthday']
        new_birthday_date = birthday_date.replace(year=year)

        while new_birthday_date < today:
            new_birthday_date = new_birthday_date.replace(year=year + 1)

        if new_birthday_date < next_week:
            birthday_date_day = new_birthday_date.weekday()
            if birthday_date_day == 5 or birthday_date_day == 6:
                new_users['Monday'].append(name)
            else:
                day = new_birthday_date.strftime('%A')
                new_users[day].append(name)

    new_users = {day: users for day, users in new_users.items() if users}
    return new_users



