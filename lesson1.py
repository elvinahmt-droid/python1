firstNumber=float(input('Enter first number: '))
secondNumber=float(input('Enter second number: '))
operation=str(input('Enter operation:(+-*/)'))
if operation=='+':
    print(firstNumber+secondNumber)
elif operation=='-':
    print(firstNumber-secondNumber)
elif operation=='/':
    if secondNumber != 0:
        print(firstNumber/secondNumber)
    else:
        print("invalid input")
elif operation=='*':
    print(firstNumber*secondNumber)
else:
    print('Invalid operation')



