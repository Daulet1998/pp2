# Create a generator that generates the squares of numbers up to some number N.
class gensquare():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a * self.a <= n:
            x = self.a
            self.a += 1
            return x**2
        else:
            raise StopIteration

n = int(input())
z = gensquare()
i = iter(z)
for c in i:
    print(c)
