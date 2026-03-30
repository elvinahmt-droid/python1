def task1():
    age = int(input("Enter your age: "))
    if age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")


def task2():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


def task3():
    score = int(input("Enter your exam score: "))
    if score >= 90:
        print("Excellent")
    elif score >= 70:
        print("Good")
    elif score >= 50:
        print("Average")
    else:
        print("Fail")


def task4():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print(a, "is greater")
    elif b > a:
        print(b, "is greater")
    else:
        print("They are equal")


def task5():
    temp = float(input("Enter temperature: "))
    if temp < 15:
        print("The weather is cold.")
    elif temp < 25:
        print("The weather is warm.")
    else:
        print("The weather is hot.")


def task6():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def task7():
    hour = int(input("Enter current hour (0-23): "))
    if hour < 12:
        print("Good morning")
    elif hour < 17:
        print("Good afternoon")
    elif hour < 21:
        print("Good evening")
    else:
        print("Good night")

def task8():
    for i in range(1, 21):
        print(i)


def task9():
    for i in range(1, 31):
        if i % 2 == 0:
            print(i)


def task10():
    for i in range(1, 26):
        if i % 2 != 0:
            print(i)


def task11():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


def task12():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(i)


def task13():
    n = int(input("Enter a number: "))
    for i in range(n, 0, -1):
        print(i)


def task14():
    total = 0
    for i in range(1, 101):
        total += i
    print("Sum =", total)

def task15():
    total = 0
    for _ in range(5):
        num = int(input("Enter a number: "))
        total += num
    print("Total sum =", total)


def task16():
    count = 0
    for _ in range(5):
        num = int(input("Enter a number: "))
        if num > 0:
            count += 1
    print("Positive numbers:", count)


def task17():
    count = 0
    for _ in range(5):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            count += 1
    print("Even numbers:", count)


def task18():
    name = input("Enter your name: ")
    print("Hello", name, "! Welcome!")


def task19():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum =", a + b)


def task20():
    num = int(input("Enter a number: "))
    print("Square =", num * num)


def task21():
    num = int(input("Enter a number: "))
    print("Cube =", num * num * num)


def task22():
    secret = 7   # You can change this number
    for _ in range(3):
        guess = int(input("Guess the secret number: "))
        if guess == secret:
            print("Correct! You guessed it.")
            return
    print("Sorry, you ran out of chances. The number was", secret)


def task23():
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Too short")
    elif len(password) < 10:
        print("Acceptable")
    else:
        print("Strong")


def task24():
    print("Enter your 3 favorite colors:")
    for _ in range(3):
        color = input()
        print(color)


def task25():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for name in names:
        print(name)

def bonus1():
    total = 0
    for _ in range(3):
        score = int(input("Enter exam score: "))
        total += score
    average = total / 3
    print("Average score =", average)


def bonus2():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)


def bonus3():
    username = input("Enter username: ")
    age = int(input("Enter your age: "))
    if age >= 13:
        print(username, "can register on the website.")
    else:
        print(username, "cannot register. Minimum age is 13.")
