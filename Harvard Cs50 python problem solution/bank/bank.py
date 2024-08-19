#taking user input
greeting = input("Greeting ").strip().lower()

#chech the condition to output the right one
match greeting:
    case _ if greeting.startswith ("hello"):
        print("$0")
    case _ if greeting.startswith ("h"):
        print("$20")
    case _:
        print("$100")

