# python program to add two numbers
print("---Simple Calculator---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("choose an operation (1-4): ")
number1 = float(input("Enter first number:"))
number2 = float(input("Enter Second number:"))
print("you chose: ", choice)
if choice == "1":
    result = number1 + number2
    print("You selected Addition, Result is:", result)
elif choice == "2":
    result = number1 - number2
    print("You Selected Subtraction, Result is:", result)
elif choice == "3":
    result = number1 * number2
    print("You selected Multiplication, Result is:", result)
elif choice == "4":
    if number2 == 0:
        print("Error. Division by zero is not allowed.")
else:
    result = number1 / number2
    print("You selected Division, Result is:", result)
