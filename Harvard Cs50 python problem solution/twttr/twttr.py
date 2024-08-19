#create a function to remove vowels
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
#Run the loop to find out the vowels
    for char in input_string:
        if char not in vowels:
            result += char
    return result
#taking use input
user_input = input("Write anything  you want: ")

#change and print the final results after remove the vowel for the input
result = remove_vowels(user_input)
print(f"Result after remove vowel: {result}")
