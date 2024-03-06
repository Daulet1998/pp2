def gensquares():
    for i in range(a, b+1):
        yield i*i
a = int(input("Enter starting point: "))
b = int(input("Enter ending point: "))
for x in gensquares():
    print(x)
