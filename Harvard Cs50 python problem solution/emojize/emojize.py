import emoji

x = input("Input: ") #taking user input

#try to get the emoji
try:
    x = emoji.emojize(x)

    #if any error arrived this will handle that
except ValueError:
    pass
#if both of the try and except failed due to alias then the else part will execute
else:
    x = emoji.emojize(x, language = "alias")

#finally print the desire emoji
print(x)
