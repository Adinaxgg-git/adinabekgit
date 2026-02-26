from datetime import datetime, timedelta
import pytz

# Current date and time
now = datetime.now()
print("Current date:", now)

# Create specific date
specific_date = datetime(2025, 1, 1)
print("Specific date:", specific_date)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Date difference
future = now + timedelta(days=10)
print("After 10 days:", future)

# Timezone example
timezone = pytz.timezone("Asia/Almaty")
tz_time = datetime.now(timezone)
print("Almaty time:", tz_time)
