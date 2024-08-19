import inflect #importing module

p = inflect.engine()

#create list to store user input
names = []

#setup a loop to get multiple input from the user
while True:
    try:
        inputname = input("enter your name: ")
        #append input name step by step in names list
        names.append(inputname)
    #exit the loop if user press ctrl + D
    except EOFError:
        print()
        break

#using module funtion to add the input name in structure way
output = p.join(names)
#finally print the expected output
print(f"Adieu, adieu, to {output}")
