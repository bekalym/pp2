#1 datetime Module
import datetime

x = datetime.datetime.now()

print(x)

#2 Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#3 Date Formatting
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#4 Calculating Time Differences

from datetime import datetime, timedelta
a = datetime(2026, 2, 25, 11, 0, 0)
b = datetime(2026, 2, 26, 13, 30, 0)
diff = b - a
print(diff)
print(diff.total_seconds())
print(a + timedelta(days=7, hours=2))

#5 Working with Timezones
from datetime import datetime
from zoneinfo import ZoneInfo
dt = datetime.now(ZoneInfo("Asia/Almaty"))
print(dt)
print(dt.astimezone(ZoneInfo("UTC")))
print(dt.astimezone(ZoneInfo("America/New_York")))

