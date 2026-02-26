from datetime import datetime, timedelta

# Task 1
now = datetime.now()
minus_five_days = now - timedelta(days=5)
print("Task 1")
print("Now:", now)
print("Minus 5 days:", minus_five_days)
print()

# Task 2
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Task 2")
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
print()

# Task 3
dt_with_micro = datetime.now()
dt_no_micro = dt_with_micro.replace(microsecond=0)
print("Task 3")
print("With microseconds:", dt_with_micro)
print("Without microseconds:", dt_no_micro)
print()

# Task 4
d1 = datetime(2026, 2, 26, 12, 0, 0)
d2 = datetime(2026, 2, 26, 15, 30, 45)
diff_seconds = int((d2 - d1).total_seconds())
print("Task 4")
print("Date 1:", d1)
print("Date 2:", d2)
print("Difference (seconds):", diff_seconds)