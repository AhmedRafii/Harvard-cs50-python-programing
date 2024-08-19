def main():
    # Initialize the amount due
    amount_due = 50

    # Keep asking for coins until the amount due is less than or equal to 0
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")

        # Prompt user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the inserted coin is an accepted denomination
        if coin in [25, 10, 5]:
            amount_due -= coin

            # If the amount due is less than zero, break out of the loop
            if amount_due <= 0:
                break

    # Calculate change owed
    change_owed = -amount_due if amount_due < 0 else 0

    # Output the change owed, if any
    print(f"Change Owed: {change_owed}")

# Call the main function
if __name__ == "__main__":
    main()
