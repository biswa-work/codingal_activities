import datetime
import calendar

city = input("Enter city: ")
temperature = float(input("Enter temperature: "))

if temperature > 30:
    print(city, "- Hot weather")
elif temperature >= 20:
    print(city, "- Pleasant weather")
else:
    print(city, "- Cold weather")

now = datetime.datetime.now()
print(now)
print(calendar.calendar(now.year))
