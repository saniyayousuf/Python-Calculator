print("-------Making Mini Calculator--------")
while True:
    userNum1 = int(input("Please enter first number  here: "))
    userNum2 = int(input("Please enter second number here: "))

    print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Mutiplication \nPress 4 for division")

    Operator = int(input("Enter your choice bwetween 1-4: "))

    # Conditional statements
    if Operator == 1:
        result = userNum1 + userNum2
        print(f"{userNum1} + {userNum2} is equal to {result}")

    elif Operator == 2:
        result = userNum1 - userNum2
        print(f"{userNum1} - {userNum2} is equal to {result}")

    elif Operator == 3:
        result = userNum1 * userNum2
        print(f"{userNum1} * {userNum2} is equal to {result}")

    elif Operator == 4:
        if userNum2 != 0: 
            result = userNum1 / userNum2
            print(f"{userNum1} / {userNum2} is equal to {result}")
        else:
            print("Division by zero is not allowed. Please enter a non-zero number for the second number.")
            continue
    else:
        print("Invalid Input. Please enter a number between 1 and 4.")
        continue

    another_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
    if another_calculation != 'y':
        break    
