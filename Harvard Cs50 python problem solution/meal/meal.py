#taking user input and convert it to hours
def main():
    user_input = input("Enter the time: ")
    time_in_hours = convert(user_input)
#checking the condition to show the perfect message
    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")

#convert user input to hours and minute and make it floating number
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) /60

if __name__ == "__main__":
    main()
