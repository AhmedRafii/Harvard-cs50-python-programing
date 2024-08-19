#taking user input
user_input = input("Enter your text here: ")

#printing sneak_case
print("sneak_case: ", end="")

#run the loop to check each letter
for char in user_input:
    if char.isupper():
        print("_" + char.lower(), end="")
    else:
        print(char, end="")

print()
