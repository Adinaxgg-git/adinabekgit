from datetime import datetime

date1 = datetime(2026, 2, 25, 12, 0, 0)
date2 = datetime(2026, 2, 24, 10, 30, 0)

difference = date1 - date2
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)