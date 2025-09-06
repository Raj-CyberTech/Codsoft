# WELCOME NOTE BY THE CREATOR OF THIS PROJECT 
print("\n~~~~ INTERNSHIP PROJECT BY CODESOFT ~~~~\n")
print("\n###### WELCOME TO THE SIMPLE CALCULATOR INTERFACE #####\n")

while True:  # Loop to allow multiple calculations
    
    # ENTERING THE INPUT FROM THE USER (FLOAT TO INCLUDE DECIMAL VALUES)
    num1 = float(input("Enter the first number :---- "))
    num2 = float(input("Enter the second number :---- "))

    # ACCEPTING OPERATION CHOICE FROM THE USER
    print("\nPress 1 for Addition (+)")
    print("Press 2 for Subtraction (-)")
    print("Press 3 for Multiplication (*)")
    print("Press 4 for Division (/)")
    
    choice = int(input("Enter your choice from 1-4:---- "))

    # PERFORMING THE CALCULATION
    if choice == 1:
        print("Result:", num1 + num2)
    elif choice == 2:
        print("Result:", num1 - num2)
    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("INVALID INPUT")

    # ASK USER IF THEY WANT TO CONTINUE 
    cont = input("\nDo you want to perform another calculation? (y/n): ").lower()
    if cont != "y":
        print("\nThank you for using the calculator. Goodbye! 👋")
        break
