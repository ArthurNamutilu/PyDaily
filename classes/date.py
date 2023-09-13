#!/usr/bin/python3
import datetime

graduation_date = datetime.date(2023, 12, 14)
yesterday_date = datetime.date(2023, 9, 12)

rem_days = (graduation_date - yesterday_date).days
print(rem_days)
