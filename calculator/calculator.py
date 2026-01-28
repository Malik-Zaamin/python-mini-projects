
# Looping until user quits
while True:
    user = input("Let us calculate (y/n): ").lower().strip()
    if user == "n":
        print("Quitting...")
        break
    elif user == "y":
        # Small design
        print("----Welcome to your CLI calculator----")
    else:
        print("Please choose y/n")
        continue
    # Handling Value_errors
    try:
        # Asking for user input ( 2 numbers )
        num1 = float(input("First digit: "))
        num2 = float(input("Second digit: "))

        # Displaying operators
        # Stripping it to remove white space for any user mistake
        operator = input("Choose your operator (+, -, *, /, **): ").strip()

        # Addition
        if operator == "+":
            print(f"The sum of {num1} and {num2} is {num1 + num2}")
        
        # Subtraction
        elif operator == "-":
            print(f"The difference of {num1} and {num2} is {num1 - num2}")
        
        # Multiplication
        elif operator == "*":
            print(f"The product of {num1} and {num2} is {num1 * num2}")
        
        # Division
        elif operator == "/":
            # Handling division by zero
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"The quotient of {num1} and {num2} is {num1 / num2}")
        
        # Exponent
        elif operator == "**":
            print(f"The power of {num1} and {num2} is {num1 ** num2}")
        
        # Invalid response
        else:
            print("Please choose a valid operator")
    except ValueError:
        print("Invalid value.")