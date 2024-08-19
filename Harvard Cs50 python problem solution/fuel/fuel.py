while True:
    try:
        # Prompt user for input
        user_input = input("Write your text: ")
        x, y = user_input.split('/')

        # Convert X and Y to integers
        x= int(x)
        y= int(y)

        # Check if the fraction is valid (X should be less than or equal to Y)# Check if the fraction is valid (X should be less than or equal to Y)
        if x > y:
            print("Invalid input. X should be less then or equal to Y.")
            continue
        # Calculate percentage
        percentage = (x / y) * 100

        # Round to nearest integer
        percentage = round(percentage)

        # Check for special cases and output result
        if percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f"{percentage}%")
            break

    # Handle invalid input and division by zero
    except (ValueError, ZeroDivisionError):
        print("Invalid input")


