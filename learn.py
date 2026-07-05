# ----- Variables and assignment -----
x = 5
print(x)
x = x + 1
print(x)
x = 100
print(x)

# ----- Arithmetic operators -----
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3)   # floor division
print(5 % 3)    # modulus (remainder)
print(10 % 2)   # even check
print(7 % 2)    # odd check

# ----- Comparison operators -----
print(5 == 3)
print(5 != 3)
print(5 > 3)
print(5 < 3)
print(5 <= 3)
print(5 >= 3)

# ----- If / elif / else -----
age = 15

if age >= 18:
    print("you are an adult")
else:
    print("You are a minor")

marks = 40
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# ----- For loops with range() -----
for i in range(5):
    print(i)

for i in range(5):
    print(i * 2)

for i in range(2, 7):
    print(i)

for i in range(0, 10, 2):
    print(i)

# ----- While loop -----
count = 0
while count < 5:
    print(count)
    count = count + 1

# ----- break and continue -----
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(6):
    if i == 3:
        continue
    print(i)

#-------Lists---------
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])    

#adding and removing from a list
fruits.append("mango")         # adds to the END of the list
print(fruits)

fruits.remove("banana")           # removes by VALUE (finds and deletes it)
print(fruits)

print(len(fruits))                 # len() tells you how many items are in the list


#----------Negative indexing-counting from the end-------

print(fruits[-1])            #last item

print(fruits[-2])            #second to last item 

#--------------slicing — grabbing a chunk of a list----------

numbers = [10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


#----------looping through a list-----

for fruit in fruits:
    print(fruit)


#--------Tules---------
coordinates = (10,20,30)
print(coordinates)
print(coordinates[0])
print(coordinates[1])    

#-----Sets-----
colors = {"red", "blue", "green" , "red", "blue"}
print(colors)
print(len(colors))

# ----checking membership in a set-
print("red" in colors)
print("yellow" in colors)

#----------removing duplicates from a list using a set
numbers = [1,2,2,3,3,3,4]
unique = list(set(numbers))
print(unique)

#-------Dictionaries--
student = {
    "name" :"Vaishnavi",
    "age" : 20,
    "city" : "Delhi"
}

print(student)
print(student["name"])
print(student["age"])

#-----adding a new key-value pair
student["grade"] = "A"
print(student)
# updating an existing value
student["age"] = 21
print(student)
# removing a key-value pair
del student["city"]
print(student)
# checking if a key exists
print("name" in student)
print("city" in student)

#-----looping through a dictionary----
for key in student:
    print(key, ":", student[key])


# ----- List Comprehensions -----
numbers = [1, 2, 3, 4, 5]

# traditional way
squared = []
for n in numbers:
    squared.append(n * 2)
print(squared)

# list comprehension
squared = [n * 2 for n in numbers]
print(squared)

# only include even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# ----- Dictionary Comprehensions -----
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

#-----------Functions-----------
def greet(name):
    print("Hello, " + name + "! Welcome.")
greet("Vaishnavi")
greet("Rahul")
greet("Priya")

def add(a, b):
    return a + b
result = add(3, 5)
print(result)


# print vs return
def add_with_print(a, b):
    print(a + b)        # just displays it, returns nothing

def add_with_return(a, b):
    return a + b        # sends the value back out

result1 = add_with_print(3, 5)
result2 = add_with_return(3, 5)

print(result1)
print(result2)

#--------------Deafult parameters--------
def greet(name, message="Welcome"):
    print("Hello, " + name + "! " + message)

greet("Vaishnavi")
greet("Rahul", "Good morning")

#--------keyword arguements----------
def describe(name, age, city):
    print(name + " is " + str(age) + " years old from " + city)

# positional — order matters
describe("Vaishnavi", 20, "Delhi")

# keyword — order doesn't matter
describe(city="Delhi", name="Vaishnavi", age=20)

# ----- Variable Scope -----
x = 100      # global variable — created outside any function

def my_function():
    y = 50   # local variable — created inside a function
    print(x) # can see x? YES — functions can read global variables
    print(y) # can see y? YES — y belongs to this function

my_function()
print(x)     # can see x? YES — x is global, visible everywhere
     # can see y? NO — y only exists inside my_function


# ----- Lambda Functions -----
# regular function
def square(n):
    return n * n

# same thing as a lambda
square_lambda = lambda n: n * n

print(square(5))
print(square_lambda(5))

# ----- map and filter -----
numbers = [1, 2, 3, 4, 5]

# map — apply a function to every item in a list
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)

# filter — keep only items where function returns True
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)

numbers = [1, 2, 3, 4, 5]

# way 1 — for loop
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# way 2 — list comprehension
evens = [n for n in numbers if n % 2 == 0]

# way 3 — filter + lambda
evens = list(filter(lambda n: n % 2 == 0, numbers))


# ----- OOP - Classes and Objects -----
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " says: Woof!")

# creating objects from the class
dog1 = Dog("Bruno", "Labrador")
dog2 = Dog("Max", "Poodle")

print(dog1.name)
print(dog2.name)
dog1.bark()
dog2.bark()

#encapsulation-------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # private variable — double underscore

    def deposit(self, amount):
        self.__balance += amount
        print(self.owner + " deposited " + str(amount))

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(self.owner + " withdrew " + str(amount))

    def get_balance(self):
        return self.__balance

account = BankAccount("Vaishnavi", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())


# ----- Inheritance -----
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

    def sleep(self):
        print(self.name + " is sleeping")

class Dog(Animal):        # Dog inherits from Animal
    def bark(self):
        print(self.name + " says: Woof!")

class Cat(Animal):        # Cat inherits from Animal
    def meow(self):
        print(self.name + " says: Meow!")

dog = Dog("Bruno")
cat = Cat("Whiskers")

dog.eat()       # inherited from Animal
dog.bark()      # Dog's own method
cat.sleep()     # inherited from Animal
cat.meow()      # Cat's own method

# ----- Polymorphism -----
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound")

class Dog(Animal):
    def speak(self):
        print(self.name + " says: Woof!")

class Cat(Animal):
    def speak(self):
        print(self.name + " says: Meow!")

class Cow(Animal):
    def speak(self):
        print(self.name + " says: Moo!")

animals = [Dog("Bruno"), Cat("Whiskers"), Cow("Daisy")]

for animal in animals:
    animal.speak()

    # ----- Abstract Classes -----
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("I am a shape with area: " + str(self.area()))

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)

c.describe()
r.describe()