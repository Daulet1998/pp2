import math
# DegTo Rad
a = int(input())
print(a * math.pi/180)

# area of trap
h = int(input())
a = int(input())
b = int(input())
print((a+b)/2*h)

# area of parall
l = int(input())
h = int(input())
print(l*h)

# PolygonArea
n = int(input())
length = int(input())
p = n * length
deg = 180/n
tang = int(math.tan(deg))
apophem = length/2/tang
area = apophem * p/2
print(area)


