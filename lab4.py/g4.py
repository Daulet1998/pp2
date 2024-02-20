#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.


def Square(a,b):
    for i in range(a,b):
        yield i**2
a=int(input())
b=int(input())
for i in Square(a,b):
    print(i)