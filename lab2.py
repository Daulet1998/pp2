# list
# 1 exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
# 2 exercise
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)
# 3 exercise
fruits.append("orange")
print(fruits)
# 4 exercise
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)
# 5 exercise
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
# 6 exercise
fruits = ["apple", "banana", "cherry"]
print(fruits[-1:])
# 7 exercise
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# 8 exercise
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
print()


# tuples
# 1 exercise
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# 2 exercise
print(len(fruits))
# 3 exercise
print(fruits[-1:])
# 4 exercise
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
print()


# sets
# 1 exercise
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
# 2 exercise
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
# 3 exercise
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
# 4 exercise
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
# 5 exercise
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


# dicts
# 1 ex
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# 2 ex
car["year"] = 2020
print(car)
# 3 ex
car["color"] = "red"
print(car)
# 4 ex
car.pop("model")
print(car)
# 5 ex
car.clear()
print(car)


# while loops
# 1 ex
i = 1
while i < 6:
    print(i)
    i += 1
# 2 ex
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# 3 ex
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# 4 ex
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# for loops
# 1 ex
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# 2 ex
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# 3 ex
for x in range(0, 6):
    print(x)
# 4 ex
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)



