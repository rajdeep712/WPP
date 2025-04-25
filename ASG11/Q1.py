import pandas as pd

datetime_obj_1 = pd.to_datetime('2012-01-15')
print(f"Date time object for Jan 15 2012: {datetime_obj_1}")

datetime_obj_2 = pd.to_datetime('2012-01-15 21:20:00')
print(f"Specific date and time of 9:20 pm: {datetime_obj_2}")

local_datetime = pd.to_datetime('now')
print(f"Local date and time: {local_datetime}")

date_only = pd.to_datetime('2012-01-15').date()
print(f"A date without time: {date_only}")

current_date = pd.to_datetime('today').date()
print(f"Current date: {current_date}")

time_from_datetime = local_datetime.time()
print(f"Time from a date time: {time_from_datetime}")

current_local_time = pd.to_datetime('now').time()
print(f"Current local time: {current_local_time}")