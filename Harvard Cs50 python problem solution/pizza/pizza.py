import sys
import csv
from tabulate import tabulate


def main():
    check_command_line()
    #variable to store the table data
    table = []
    #try to open the csv file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    #Handle if any error arrived
    except FileNotFoundError:
        sys.exit("File does not exist")
    #print the table as needed
    print(tabulate(table[1:], headers = table[0], tablefmt = "grid"))

#define a funtion to check the elements in command line
def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #if the file is not csv 
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
