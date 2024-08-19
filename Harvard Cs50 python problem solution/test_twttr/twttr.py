def main():
    user_input = input("Write anything: ")
    no_vowel = shorten(user_input)
    print(f"Output is: {no_vowel}")


def shorten(word):
    final_output = ""
    for char in word:
        if not char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            final_output += char
    return final_output


if __name__ == "__main__":
    main()
