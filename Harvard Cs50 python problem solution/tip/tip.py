def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    float_number = float(d.replace('$', ''))
    return float_number


def percent_to_float(p):
    # TODO
    percent_float = float(p.replace('%', '')) / 100
    return percent_float


main()
