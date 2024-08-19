#creating function for change text emoticons to graphic emoticons
def convert(value):
    result = value.replace(':)', '🙂').replace(':(', '🙁')
    return result

#Taking user input 
def main():
    user_input = input("Enter your text")
    final_result = convert(user_input)
    print(final_result)

main()
