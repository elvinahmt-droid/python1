name = "Elvin"
age = 15
average_score = 88.5

print(name)
print(age)
print(average_score)
print(type(name))
print(type(age))
print(type(average_score))

name = input("Enter your name: ")
print("Hello,", name)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print("Sum:", sum_result)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Floor division:", x // y)

word = input("Enter one word: ")
print(type(word))

integer_number = int(input("Enter an integer number: "))
float_number = float(input("Enter a float number: "))

print("Type of the integer number:", type(integer_number))
print("Type of the float number:", type(float_number))

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print("Are they equal?", n1 == n2)
print("Are they different?", n1 != n2)
print("Is first greater?", n1 > n2)
print("Is second greater?", n2 > n1)

p = float(input("Enter first number: "))
q = float(input("Enter second number: "))

print("First >= second?", p >= q)
print("Second <= first?", q <= p)

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Both positive?", x > 0 and y > 0)
print("At least one positive?", x > 0 or y > 0)
print("First is not positive?", not (x > 0))

score1 = float(input("Enter first exam score: "))
score2 = float(input("Enter second exam score: "))

total = score1 + score2
average = total / 2

print("Sum:", total)
print("Average:", average)
print("First is greater?", score1 > score2)
print("Second is greater?", score2 > score1)

width = float(input("Enter width: "))
length = float(input("Enter length: "))

area = width * length
perimeter = 2 * width + 2 * length

print("Area:", area)
print("Perimeter:", perimeter)

seconds = int(input("Enter seconds: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(seconds, "seconds =", minutes, "minutes", remaining_seconds, "seconds")

age = int(input("Enter your age: "))

print("Greater than 18?", age > 18)
print("Equal to 18?", age == 18)
print("Less than 18?", age < 18)

number = int(input("Enter a number: "))

print("Even?", number % 2 == 0)
print("Odd?", number % 2 != 0)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Sum:", a + b + c)
print("Product:", a * b * c)
print("First equal to second?", a == b)

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponent:", x ** y)
print("Floor division:", x // y)

print("Both > 10?", x > 10 and y > 10)
print("One < 0?", x < 0 or y < 0)
print("First not negative?", not (x < 0))

a = float(input("Number 1: "))
b = float(input("Number 2: "))

print("Both greater than 10?", a > 10 and b > 10)
print("One of them less than 0?", a < 0 or b < 0)
print("First not negative?", not (a < 0))

name = input("Enter name: ")
age = input("Enter age: ")
color = input("Enter favorite color: ")

print("My name is", name + ",", "I am", age, "years old, and my favorite color is", color + ".")

num = float(input("Enter a number: "))

print("Square:", num * num)
print("Cube:", num * num * num)

x = float(input("First number: "))
y = float(input("Second number: "))

print("Results:")
print("Addition       :", x + y)
print("Subtraction    :", x - y)
print("Multiplication :", x * y)
print("Division       :", x / y)
print("Modulus        :", x % y)
print("Power          :", x ** y)
print("Floor division :", x // y)
print("---------------------")
print("Equal?         :", x == y)
print("Greater?       :", x > y)
print("Less?          :", x < y)
print("Both positive? :", x > 0 and y > 0)