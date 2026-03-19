# 🧮 Basic Calculator

A simple, beginner-friendly Python calculator that performs basic arithmetic operations. Perfect for learning Python fundamentals while building something useful!

## 📋 Overview

This calculator project provides a clean, command-line interface for performing basic mathematical operations. Built with Python's standard library, it's an excellent starting point for beginners learning programming concepts.

## ✨ Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Error Handling**: Prevents crashes from invalid inputs
- **Division by Zero Protection**: Graceful error messages
- **User-Friendly Interface**: Clear prompts and formatted output
- **No Dependencies**: Uses only Python standard library
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher installed on your system
- No additional packages required!

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/basic-calculator.git
cd basic-calculator
```

2. **Or download directly**
```bash
curl -O https://raw.githubusercontent.com/yourusername/basic-calculator/main/calculator.py
```

3. **Run the program**
```bash
python calculator.py
```

## 💻 Usage

### Basic Operation
```
========================================
          BASIC CALCULATOR
========================================
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
========================================
Enter your choice (1-5): 1

Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
```

### Example Session
```
Enter your choice (1-5): 4
Enter first number: 10
Enter second number: 3
10.0 / 3.0 = 3.3333333333333335

Press Enter to continue...
```

## 📁 Project Structure

```
basic-calculator/
│
├── calculator.py          # Main calculator program
├── README.md              # This file
├── LICENSE                # MIT License
└── .gitignore             # Git ignore file
```

## 📝 Code

```python
# calculator.py - Basic Calculator

def show_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("          BASIC CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    """Get two numbers from user with error handling"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("❌ Error: Please enter valid numbers!")
        return None, None

def addition():
    """Perform addition"""
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

def subtraction():
    """Perform subtraction"""
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

def multiplication():
    """Perform multiplication"""
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

def division():
    """Perform division with zero check"""
    num1, num2 = get_numbers()
    if num1 is not None:
        if num2 == 0:
            print("❌ Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

def main():
    """Main program loop"""
    print("Welcome to the Basic Calculator!")
    
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
            print("👋 Thanks for using the calculator. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

## 🎓 Learning Outcomes

This project helps you learn:

| Concept | Implementation |
|---------|---------------|
| **Functions** | Each operation in its own function |
| **User Input** | `input()` function with type conversion |
| **Conditionals** | `if/elif/else` for menu and operations |
| **Loops** | `while` loop for continuous operation |
| **Error Handling** | `try/except` for invalid inputs |
| **String Formatting** | f-strings for clean output |
| **Modular Design** | Separate functions for each task |

## 🔧 Customization Options

### Add More Operations
```python
def power():
    """Add exponentiation"""
    num1, num2 = get_numbers()
    if num1 is not None:
        result = num1 ** num2
        print(f"{num1} ^ {num2} = {result}")

def modulus():
    """Add remainder"""
    num1, num2 = get_numbers()
    if num1 is not None and num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
```

### Change Decimal Places
```python
# For 2 decimal places
print(f"{num1} + {num2} = {result:.2f}")

# For scientific notation
print(f"{num1} + {num2} = {result:.2e}")
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions
- Add more mathematical operations (power, square root, modulus)
- Create a GUI version with tkinter
- Add calculation history feature
- Implement memory functions (M+, M-, MR, MC)
- Add keyboard shortcuts
- Create a web version with Flask

## 📊 Project Status

- **Current Version**: 1.0.0
- **Stability**: Stable
- **Maintenance**: Active
- **Python Version**: 3.6+

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 👨‍💻 Author

**Your Name**
- GitHub: [@mobrahi](https://github.com/yourusername)
- Twitter: [@faairuz](https://twitter.com/yourtwitter)

## 🙏 Acknowledgments

- Inspired by countless beginners learning Python
- Built with Python's amazing standard library
- Thanks to all contributors and users

## 📚 Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)

## ❓ FAQ

**Q: Do I need to install anything?**
A: No! Python comes with everything you need.

**Q: Why do I get an error when entering letters?**
A: The calculator expects numbers. Entering text causes a ValueError, which is handled gracefully.

**Q: Can I use decimal numbers?**
A: Yes! Enter numbers like 3.14 or 2.5 - they work perfectly.

**Q: How do I exit the program?**
A: Choose option 5 from the menu, or press Ctrl+C.

**Q: Can I see previous calculations?**
A: The basic version doesn't include history, but it's a great feature to add!

## 🎯 Next Steps

Once you're comfortable with this project, try:
1. **Adding more operations** (power, square root)
2. **Creating a GUI version** with tkinter
3. **Adding a history feature** to see past calculations
4. **Implementing memory functions**
5. **Building a scientific calculator**

## ⭐ Support

If you found this project helpful:
- Give it a ⭐ on GitHub
- Share it with fellow learners
- Contribute improvements
- Report issues or suggest features

---

**Made with ❤️ and Python** 🐍

---

*Happy Calculating!* 🧮
