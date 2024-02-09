# TSIS
1)

class with2meth:
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


UserInput = with2meth()
UserInput.getString()
UserInput.printString()

2)

class Shape:
    def init(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def init(self, l):
        self.length = l

    def area(self):
        a = self.length * self.length
        return a


s = Square(int(input()))
print(s.area())

3)

class Shape:
    def init(self):
        pass

    def area(self):
        return 0


class Rectangle(Shape):
    def init(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle(int(input()), int(input()))
print(r.area())

4)import math


class Point:
    def init(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        return Point(self.x, self.y)

    def dist(self):
        return math.sqrt((self.x)
        2 + (self.y)
        2)


        xy = Point(int(input()), int(input()))
        Point.show(xy)

        distance = Point.dist(xy)
        print(distance)

        xy = Point.move(xy, int(input()), int(input()))
        Point.show(xy)

        5)

        class Bank_account:
            def init(self, owner, balance):
                self.owner = owner
                self.balance = balance

            def deposit(self):
                print("Please, enter the sum you want to put in deposit:")
                money = float(input())
                self.balance += money
                return Bank_account(self.owner, self.balance)

            def withdraw(self):
                print("Please, enter the sum you want to take:")
                taken = float(input())
                while taken > self.balance:
                    print("Please, enter the sum you want to take:")
                    taken = float(input())
                self.balance -= taken
                return Bank_account(self.owner, self.balance)

            def str(self):
                return f"{self.owner} have {self.balance} money in his deposit."

        account = Bank_account(input(), float(input()))
        account = Bank_account.deposit(account)
        account = Bank_account.withdraw(account)
        print(account)

        6)

        def filter_prime(number):
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True

        n = int(input())
        l = []
        for i in range(n):
            x = int(input())
            l.append(x)
        primes = list(filter(filter_prime, l))
        print(primes)
        Functions
        Pt1
        1 )

        def gramtoounce(a):
            ounces = 28.3495231 * a
            return ounces

        a = int(input())
        print(gramtoounce(a))

        2)

        def temperature(f):
            c = (5 / 9) * (f - 32)
            return c

    far = int(input())
    print(temperature(far))

    3 )

    def solve(numlegs, numheads):
        for i in range(1, numheads + 1):
            if (i * 4) + (numheads - i) * 2 == numlegs:
                ans = f"{i} rabbits,{numheads - i} chickens"
                return ans

    print("Enter number of legs:")
    numlegs = int(input())
    print("Enter number of heads")
    numheads = int(input())
    print(solve(numlegs, numheads))
    4 )

    def filter_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    print("Enter size of list:")
    n = int(input())
    print("Enter elements of list:")
    l = list()
    for i in range(n):
        x = int(input())
        if filter_prime(x):
            l.append(x)
    print(l)

    5 )

    def factorial(a):
        fact = 1
        for i in range(1, a + 1):
            fact = fact * i
        return fact

    permut = str(input())
    print(factorial(len(permut)))

    6 )

    def reverse(w):
        rev = w.split()
        return ' '.join(reversed(rev))

    w = str(input())
    print(reverse(w))
    7 )

    def has_33(nums):
        return any(nums[i + 1] == nums[i] == 3 for i in range(len(nums) - 1))

    nums = list(map(int, input().split()))
    print(has_33(nums))

    8 )

    def spy_game(nums1):
        a = ''.join(nums1)
        for i in nums1:
            if '007' in a:
                return True
        return False

    nums1 = list(map(str, input().split()))
    print(spy_game(nums1))

    9 )
    import math
    def volume(r):  # V = 4pir^3/3
        vol = (4 * math.pi * r ** 3) / 3
        return vol

    r = float(input())
    print(volume(r))

    10)

    def unique_list(l):
        empty = []
        for a in l:
            if a not in empty:
                empty.append(a)
        return empty

    list1 = list(map(int, input().split()))
    print(unique_list(list1))
    11)

    def palindrome(w):
        if w == w[::-1]:
            return "Yes, it is palindrome"
        else:
            return "Not palindrome"

    w = str(input())
    print(palindrome(w))

    12)

    def histogram(list):
        for i in range(0, len(list)):
            print('*' * list[i])
        return

    list2 = list(map(int, input().split()))
    print(histogram(list2))
    13)
    import random
    number = random.randrange(1, 20)
    cnt = 1
    name = str(input("Hello! What is your name?\n"))
    print('Well', name, "I am thinking of a number between 1 and 20. Take a guess.", sep=", ")
    UserNum = int(input())

    while UserNum != number:
        if UserNum > number:
            print("Your guess is too high.")
            cnt += 1
        elif UserNum < number:
            print("Your guess is too low.")
            cnt += 1
        UserNum = int(input("Take a guess.\n"))
    print("Good job,", name, "You guessed my number in", cnt, "guesses!")

    Functions
    Pt
    2
    movies = [
        {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
        {"name": "Hitman", "imdb": 6.3, "category": "Action"},
        {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
        {"name": "The Help", "imdb": 8.0, "category": "Drama"},
        {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
        {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
        {"name": "Love", "imdb": 6.0, "category": "Romance"},
        {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
        {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
        {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
        {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
        {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
        {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
        {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
        {"name": "We Two", "imdb": 7.2, "category": "Romance"}
    ]

    # Task 1: Check if IMDB score of a movie is above 5.5
    def is_above_5_5(movie):
        return movie["imdb"] > 5.5

    # Task 2: Return sublist of movies with IMDB score above 5.5
    def above_5_5_movies(movie_list):
        return [movie for movie in movie_list if is_above_5_5(movie)]

    # Task 3: Return movies under a specific category
    def movies_by_category(category, movie_list):
        return [movie for movie in movie_list if movie["category"] == category]

    # Task 4: Calculate average IMDB score of a list of movies
    def average_imdb_score(movie_list):
        if not movie_list:
            return 0
        total_score = sum(movie["imdb"] for movie in movie_list)
        return total_score / len(movie_list)

    # Task 5: Calculate average IMDB score of movies in a specific category
    def average_imdb_score_by_category(category, movie_list):
        category_movies = movies_by_category(category, movie_list)
        return average_imdb_score(category_movies)

    # Example usage:
    print(is_above_5_5(movies[0]))  # Output: True
    print(above_5_5_movies(movies))  # Output: List of movies with IMDB score above 5.5
    print(movies_by_category("Romance", movies))  # Output: List of romance movies
    print(average_imdb_score(movies))  # Output: Average IMDB score of all movies
    print(average_imdb_score_by_category("Romance", movies))  # Output: Average IMDB score of romance movies