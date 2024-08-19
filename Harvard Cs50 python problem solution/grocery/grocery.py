def main():
    grocery = {} # Initialize an empty dictionary to store grocery items and their counts
    while True:
        try:
            item = input().lower() # Read input (item name) and convert to lowercase
            if item in grocery:
                grocery[item] += 1 # Increment count if item already exists in the dictionary
            else:
                grocery[item] = 1 # Add item to the dictionary with an initial count of 1
        except EOFError:
            # Print the grocery list with counts, sorted alphabetically by item name
            for key in sorted(grocery.keys()):
                print(grocery[key], key.upper())
            break

if __name__ == "__main__":
    main()
