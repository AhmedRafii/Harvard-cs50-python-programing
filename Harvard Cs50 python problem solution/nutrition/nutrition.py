# Main function to get user input and display calorie content
def main():
    # Get fruit name from user input, remove whitespace and convert to lowercase
    fruit = input("Enter the name of a fruit: ").strip().lower()
    # Retrieve calorie information for the given fruit
    calories = get_calories(fruit)

    # If calorie information is found, print it
    if calories is not None:
        print(f"The calorie content of {fruit} is {calories} calories.")


# Function to get the calorie content of a fruit
def get_calories(fruit):
    # Dictionary containing fruits and their respective calorie content
    fruit_calories = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lime" : 20,
        "lemon" : 15,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80
    }

    # Check if the fruit is in the dictionary and return its calorie content
    if fruit in fruit_calories:
        return fruit_calories[fruit]
    # If fruit is not found, return None
    else:
        return None

# Check if the script is run directly (not imported) and call main function
if __name__ == "__main__":
    main()
