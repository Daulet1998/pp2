username = input("Enter username: ")
print("Username is: " + username)

print("Hello, world")

if 5 > 2:
    print("Five is greater than two!")

# this is a comment
# print("Hello, World")

"""
This is a comment
written in 
more just one line
"""

x = 4
y = 'Marina'
print(x)
print(y)

# casting
x = int(3)
y = int(4.2)
z = int("3")
print(x, y, z)

a = float(7)
b = float(5.6)
c = float("8")
print(a, b, c)

d = str("s1")
e = str(0.2)
f = str(3)
print(d, e, f)

x = 10
print(type(x))
y = b"Marina"
print(type(y))

# int
x = 1215521313
y = -1651641563
print(type(x))
print(type(y))

# float
x = 15.2654
y = -15245.454
z = -515e566
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 12.5
z = 1j

a = float(x)
b = int(y)
c = complex(x)
# we cannot change complex numbers into other number types

print(a, b, c)

import random
print(random. randrange(1, 10))


# booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 5
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


x = "Hello"   # only empty strings are False
y = 20        # only 0 int is False
z = (["apple", "cherry", "banana"])

print(bool(x))
print(bool(y))
print(bool(z))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def Marina():
    return False
print (Marina())

# checking int or not
m = 200
print(isinstance(m, int))

print(10+5)

a = "Hello, World"
print(a[2:5])


b = "Hello, World!"
print(b[:5])

c = "Hello, World"
print(c[2:])

d = "Hello, World"
print(d[-5:-2])

a = "Marina"
print(a.upper())

b = "KBTUSTUDENT"
print(b.lower())

c = " lovecoding  "
print(c.strip())

d = "Hello, everyone"
print(d.replace("H", "J"))

e = "Hello, everyone"
print(e.split())

# string concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# format strings
age = 18
txt = "My name is Marina and I am {}"
print(txt.format(age))

food1 = "apple"
food2 = "humburger"
food3 = "manty"
dinner = "I want to eat {2} and {0} and {1}"
print(dinner.format(food1, food2, food3))
