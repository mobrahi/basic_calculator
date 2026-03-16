# calculator_v2.py - Menu-Based Calculator

def show_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("      BASIC CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    """Get two numbers from user"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def addition():
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

def subtraction():
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

def multiplication():
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

def division():
    num1, num2 = get_numbers()
    if num1 is not None:
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        print("Thanks for using the calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-5.")
    
    input("\nPress Enter to continue...")