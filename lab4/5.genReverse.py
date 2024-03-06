# Implement a generator that returns all numbers from (n) down to 0.
def rev():
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter any number: "))
for x in rev():
    print(x)

