menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.00

try:
    while True:
        user_input = input("Enter Your Food Name (Ctrl-D to finish):: ").strip().title()
        if user_input in menu:
            total_cost += menu[user_input]
            print(f"Your total cost is: ${total_cost:.2f}")
        else:
            print("Food in not availabe")
except EOFError:
    print(f"Your total cost is: ${total_cost:.2f}")


