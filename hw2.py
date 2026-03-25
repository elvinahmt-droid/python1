age = int(input("Enter your age: "))

if age > 18:
    print("You can sign up on our webpage.")
elif age == 18:
    print("You can sign up on our webpage, but you are not an adult.")
else:
    print("Sorry, you cannot sign up on our webpage.")

score = int(input("Enter your exam score: "))

if score >= 91 and score <= 100:
    print("A")
elif score >= 81 and score <= 90:
    print("B")
elif score >= 71 and score <= 80:
    print("C")
elif score >= 61 and score <= 70:
    print("D")
elif score >= 51 and score <= 60:
    print("E")
elif score >= 0 and score <= 50:
    print("F")
else:
    print("Invalid grade point.")

num = int(input("Enter one number: "))

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

num = int(input("Enter one number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation type (+, -, *, /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operation type.")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The first number is greater.")
elif b > a:
    print("The second number is greater.")
else:
    print("The numbers are equal.")

temp = float(input("Enter temperature: "))

if temp > 30:
    print("It is hot.")
elif temp >= 20 and temp <= 30:
    print("The weather is nice.")
else:
    print("It is cold.")

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
else:
    print("The number is not divisible by both 2 and 3.")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid username or password.")

amount = float(input("Enter shopping amount: "))

if amount >= 100:
    print("You get a discount.")
else:
    print("No discount.")

num = int(input("Enter a number: "))

if num > 100:
    print("Large number")
elif num >= 50 and num <= 100:
    print("Medium number")
else:
    print("Small number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is the largest")
elif b >= a and b >= c:
    print("Second number is the largest")
else:
    print("Third number is the largest")

day = int(input("Enter day score: "))
homework = int(input("Enter homework score: "))

if day >= 50 and homework >= 50:
    print("Passed")
else:
    print("Failed")

year = int(input("Enter a year: "))

if year < 2000:
    print("Old year")
else:
    print("New year")

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")

