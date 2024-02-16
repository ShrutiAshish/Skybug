# calculator

print("welcome to mini project Calculator design")

# Takeing user Input what operation he want to perform
# Addition = 1
# Substraction = 2
# Multiplication = 3
# Division = 4


n = int(input("Enter the number between 1 to 5 to perform a particular operation \n 1. Addition \n 2. Substraction \n 3.Multipilcation \n 4. Division \n"))

# Enter the first Number
a = int(input("Enter the first Number \n"))
b = int(input("Enter the second Number \n"))

if n == 1:
    print(f'Addidtion of the Two Number {a} + {b} is : {a+b}')
elif n == 2:
    print(f'Substraction of the Two Number {a} - {b} is : {a-b}')
elif n == 3:
    print(f'Multipilcation of the Two Number  {a} * {b} is : {a*b}')
elif n == 4:
    print(f'Division of the Two Number {a} / {b} is : {a//b}')
else:
    print(f'Please Choose the correct Operation ')