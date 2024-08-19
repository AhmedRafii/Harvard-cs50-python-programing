import random

#Define a main function to get the final result
def main():
    score = generate_integer(get_level())
    print(f"Final Score is: {score}")

#Taking the desire level from the user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            return level
        except ValueError:
            pass

#generate math according to the level selected
def generate_integer(level):
    score = 0
    for i in range(10):
        trials = 0
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        #check the user answer and filter it to know R or W
        while True:
            print(f"{x} + {y} = ", end = "")
            answer = int(input())
            if answer == x + y:
                score += 1
                break
            elif answer != (x + y) and trials !=2:
                print("EEE")
                trials +=1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
                break

    return score


if __name__ == "__main__":
    main()
