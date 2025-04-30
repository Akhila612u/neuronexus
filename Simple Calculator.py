# Simple Calculator

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the operation choices
print("Select the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Prompt the user for an operation choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform the selected operation
if choice == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")


