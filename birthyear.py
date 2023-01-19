import datetime
current_year=datetime.date.today()
year=current_year.year
dob=int(input("Enter the year of birth?"))
bdob=year-dob
print('Your Age is',bdob)