def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    has_digit = False
    for char in s:
        if char.isalpha():
            if has_digit:
                # If an alphabet appears after a digit, it's invalid
                return False
        elif char.isdigit():
            if char == "0" and not has_digit:
                # '0' should not be the first digit
                return False
            has_digit = True
        else:
            # If there's any non-alphanumeric character
            return False

    return True


main()
