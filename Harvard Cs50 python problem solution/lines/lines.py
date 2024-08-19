import sys

def main():
    check_command_line()
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exit")

    line_count = 0
    for line in lines:
        if check_line(line) == False:
            line_count += 1
    print(line_count)


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False


if __name__ == "__main__":
    main()

