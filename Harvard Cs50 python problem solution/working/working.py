import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define a regex pattern to match the valid time format
    pattern = re.compile(
        r"^(1[0-2]|0?[1-9]):?([0-5]?[0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5]?[0-9])? (AM|PM)$",
        re.IGNORECASE
    )
    match = pattern.match(s.strip())
    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    if start_minute >= 60 or end_minute >= 60:
        raise ValueError("Invalid minute value")

    start_time = convert_time_24hr(int(start_hour), start_minute, start_period)
    end_time = convert_time_24hr(int(end_hour), end_minute, end_period)

    return f"{start_time} to {end_time}"

def convert_time_24hr(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
