# dates.py
from datetime import datetime, timedelta

# 1. Subtract five days from current date
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("Five days ago:", five_days_ago)

# 2. Print yesterday, today, tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3. Drop microseconds from datetime
now_without_microseconds = today.replace(microsecond=0)
print("Now without microseconds:", now_without_microseconds)

# 4. Calculate two date difference in seconds
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 25, 12, 0, 0)
difference_seconds = (date2 - date1).total_seconds()
print("Difference in seconds:", difference_seconds)