i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

i = 10
while i >= 1:
    print(i)
    i -= 1

n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1

for i in range(1, 16):
    print(i)

for i in range(5, 26, 5):
    print(i)

for i in range(20, 0, -1):
    print(i)

for i in range(1, 31):
    if i % 2 != 0:
        print(i)

count = 0
for i in range(1, 11):
    count += 1
print("Total numbers:", count)

count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
print("Even numbers:", count)

count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print("Divisible by 3:", count)

total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)

n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)

total = 0
for i in range(1, 51):
    if i % 3 == 0:
        total += i
print("Sum:", total)

while True:
    answer = input("Type 'yes': ").strip().lower()
    if answer == "yes":
        print("Thank you!")
        break

while True:
    num = int(input("Enter a number greater than 5: "))
    if num > 5:
        print("Correct!")
        break
    else:
        print("Try again.")

while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        print("Accepted:", num)
        break
    else:
        print("Please enter a positive number.")

for i in range(1, 21):
    if i % 4 == 0:
        print(i)

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

total = 0
for i in range(1, 51):
    if i % 2 != 0:
        total += i
print("Sum of odd numbers:", total)

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print("Count:", count)

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

for i in range(1, 6):
    print(f"\nMultiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")

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

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

total = 0
for _ in range(5):
    total += int(input("Enter a number: "))
print("Sum:", total)

numbers = []
for _ in range(5):
    numbers.append(int(input("Enter a number: ")))
print("Largest:", max(numbers))

count = 0
for _ in range(5):
    if int(input("Enter a number: ")) % 2 == 0:
        count += 1
print("Even numbers:", count)

total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total sum:", total)

words = []
while True:
    word = input("Enter a word (type 'stop' to end): ").strip()
    if word.lower() == "stop":
        break
    words.append(word)
print("You entered:", words)

pos = 0
neg = 0
for _ in range(10):
    num = int(input("Enter a number: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print("Positive:", pos, "Negative:", neg)

evens = []
odds = []
for i in range(1, 51):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print("Even:", evens)
print("Odd:", odds)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

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