def main():
    while True:
        try:
            user_input = input("Write the number here: ")
            fraction = convert(user_input)
            output = gauge(fraction)
            print(output)
            break
        except (ValueError, ZeroDivisionError) as e:
            print(f"Invalid input: {e}")

def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    if x > y:
        raise ValueError("Invalid input. X should be less than or equal to Y.")

    percentage = (x / y) * 100
    return round(percentage)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
