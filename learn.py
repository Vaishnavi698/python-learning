x = 5
print(x)
x = x+1
print(x)
x = 100
print(x)

print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)
print(5%3)
print(10%2)
print(7%2)

print(5==3)
print(5!=3)
print(5>3)
print(5<3)
print(5<=3)
print(5>=3)


age = 15

if age >=18:
    print("you are an adult")
else:
    print("You are a minor")   


marks = 40
if marks >=90:
    print("Grade A")
elif marks >=75:
    print("Grade B") 
elif marks>=50:
    print("Grade C")
else:
    print("Fail")   


for i in range(5):
    print(i)      

for i in range(5):
    print(i*2)             

for i in range(2,7):
    print(i)  

for i in range(0,10,2):
    print(i)       

count = 0
while count < 5:
    print(count)
    count = count+1  

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(6):
    if i ==3:
        continue
    print(i)

  
