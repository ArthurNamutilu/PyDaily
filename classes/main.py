#!/usr/bin/python3
import datetime
"""More classes"""
class User():
    """
    class defining user storing user's name & birthday age method
    """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # Extracting First & Lastname 
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def get_age(self):
        """ Return user's age in years """
        today = datetime.date(2023, 9, 13)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("Arthur Namutilu", "19981218")
print(user.get_age())
