# List of month names for conversion from text to number
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Infinite loop to continuously prompt for user input
while True:
    # Prompt the user to enter a date
    date = input("Date: ").strip()  # Strip any leading/trailing whitespace
    try:
        # Check if the input date contains '/'
        if "/" in date:
            mm, dd, yyyy = date.split("/")  # Split the date by '/'
        elif "," in date:
            mmdd, yyyy = date.split(", ")  # Split the date by ', '
            mm, dd = mmdd.split(" ")  # Split the month and day by space
            mm = (months.index(mm)) + 1  # Convert month name to month number
        # Check if the month and day are within valid ranges
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError  # Raise an error if month or day are out of valid range
    except (AttributeError, ValueError, NameError, KeyError):
        # If any exception occurs, pass to prompt the user again
        pass
    else:
        # Print the formatted date in YYYY-MM-DD format and break the loop
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break
