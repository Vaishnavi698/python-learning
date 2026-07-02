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