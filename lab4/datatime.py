from datetime import datetime, timedelta
# substract 5 days

print("Current time:", datetime.now())
print("Five days before:", datetime.now() - timedelta(days = 5))

# yesterday, today, tomorrow
yest = datetime.now() - timedelta(1)
today = datetime.now()
tom = datetime.now() + timedelta(1)
print("Yesterday:", yest.strftime('%d-%m-%Y'))
print("Today:", today.strftime('%d-%m-%Y'))
print("Tomorrow:", tom.strftime('%d-%m-%Y'))

# microseconds
x = datetime.now()
print("Microseconds:", x.replace(microsecond=0))

# date difference
y1, m1, d1 = int(input()), int(input()), int(input())
y2, m2, d2 = int(input()), int(input()), int(input())
a = datetime(y1, m1, d1)
b = datetime(y2, m2, d2)
d = b - a
print((b-a).total_seconds())

