#Get the user input
expression = input("Enter the expression: ")
#Convert this into variables
x, y, z = expression.split(" ")
#Change input to float
x = float(x)
z = float(z)
#Calculate the number
match y:
    case '+':
        print(f'{x + z:.1f}')
    case '-':
        print(f'{x - z:.1f}')
    case '*':
        print(f'{x * z:.1f}')
    case '/':
        print(f'{x / z:.1f}')
    case _:
        print("Invalid")

