#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta 
x=datetime.now()
b=timedelta(days=5)
c=x-b
print(c.strftime("%d.%m.%Y"))