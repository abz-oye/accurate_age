import datetime

year = int(input("What year were you born in?: "))
month = int(input("What month were you born in?: "))
day = int(input("What day were you born on?: "))

DOB = datetime.datetime(year, month, day)
age = datetime.datetime.now() - DOB

age_years = age.days/365
age = str(round(age_years, 7))

print("\nYou are " + age + " years old as of today!\n")
