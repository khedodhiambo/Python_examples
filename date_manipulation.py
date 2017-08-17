import datetime

# currentDate = datetime.date.today()

# print(currentDate.year)
# print(currentDate.month)
# print(currentDate.day)
# print(currentDate.strftime('%a %d %B, %Y'))


userDate = input("Enter that magic day(dd/mm/yyyy): ")   # 12/05/2016
startDays = datetime.datetime.strptime(userDate, '%d/%m/%Y').date()
currentDate = datetime.date.today()
numDays = currentDate - startDays
print(numDays.days)
currentTime = datetime.datetime.now()
print(currentTime)
# print(numDays)
# print(datetime.date.today())


# userInput = input("Enter your birth day(dd/mm/yyyy): ")
# birthday = datetime.datetime.strptime(userInput, "%d/%m/%Y").date()
# print(birthday)
# print("Your birthday is on " + birthday)
