#trip expenditure using datetime module
import datetime
start_date = datetime.datetime(2023, 10, 1)
end_date = datetime.datetime(2023, 10, 15)
trip_duration = end_date - start_date
daily_expense = 100  # Assuming a daily expense of $100
total_expense = trip_duration.days * daily_expense
print(f"Trip Duration: {trip_duration.days} days")
print(f"Total Trip Expenditure: ${total_expense}")  