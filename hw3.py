print("1.")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\n2.")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

print("\n3.")
i = 10
while i >= 1:
    print(i)
    i -= 1

print("\n4.")
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1

print("\n5.")
for i in range(1, 16):
    print(i)

print("\n6.")
for i in range(5, 26, 5):
    print(i)

print("\n7.")
for i in range(20, 0, -1):
    print(i)

print("\n8.")
for i in range(1, 31):
    if i % 2 != 0:
        print(i)

print("\n9.")
count = 0
for i in range(1, 11):
    count += 1
print("Total numbers:", count)

print("\n10.")
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
print("Even numbers:", count)

print("\n11.")
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print("Divisible by 3:", count)

print("\n12.")
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

print("\n13.")
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)

print("\n14.")
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)

print("\n15.")
total = 0
for i in range(1, 51):
    if i % 3 == 0:
        total += i
print("Sum:", total)

print("\n16.")
while True:
    answer = input("Type 'yes': ").strip().lower()
    if answer == "yes":
        print("Thank you!")
        break

print("\n17.")
while True:
    num = int(input("Enter a number greater than 5: "))
    if num > 5:
        print("Correct!")
        break
    else:
        print("Try again.")

print("\n18.")
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        print("Accepted:", num)
        break
    else:
        print("Please enter a positive number.")

print("\n19.")
for i in range(1, 21):
    if i % 4 == 0:
        print(i)

print("\n20.")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

print("\n21.")
total = 0
for i in range(1, 51):
    if i % 2 != 0:
        total += i
print("Sum of odd numbers:", total)

print("\n22.")
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print("Count:", count)

print("\n23.")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

print("\n24.")
for i in range(1, 6):
    print(f"\nMultiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

print("\n28.")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")

print("\n29.")
n = int(input("Enter a number: "))
if n > 1:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not prime")
else:
    print("Not prime")

# 30. Print all prime numbers from 1 to 100
print("\n30.")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

print("\n31.")
total = 0
for _ in range(5):
    total += int(input("Enter a number: "))
print("Sum:", total)

print("\n32.")
numbers = []
for _ in range(5):
    numbers.append(int(input("Enter a number: ")))
print("Largest:", max(numbers))

print("\n33.")
count = 0
for _ in range(5):
    if int(input("Enter a number: ")) % 2 == 0:
        count += 1
print("Even numbers:", count)

print("\n34.")
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total sum:", total)

print("\n35.")
words = []
while True:
    word = input("Enter a word (type 'stop' to end): ").strip()
    if word.lower() == "stop":
        break
    words.append(word)
print("You entered:", words)

print("\n36.")
pos = 0
neg = 0
for _ in range(10):
    num = int(input("Enter a number: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print("Positive:", pos, "Negative:", neg)

print("\n37.")
evens = []
odds = []
for i in range(1, 51):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print("Even:", evens)
print("Odd:", odds)

print("\n38.")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("\n39.")
secret = 7
print("Guess the secret number!")
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Congratulations! You guessed it.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")