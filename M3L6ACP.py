#months using datetime module
import datetime
current_date = datetime.datetime.now()
month_name = current_date.strftime("%B")
print("Current month:", month_name) 