# Write a program using generator to print
# the even numbers between 0 and n in comma
# separated form where n is input from console.
def even():
    for i in range(0, n+1, 2):
        yield i
n = int(input())
res = []
for x in even():
    res.append(str(x))
print(",". join(res))
