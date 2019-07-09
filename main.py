import os
os.system('cls')
while True:
    command = input("Please open the shop with /shop!\n\n")
    if command.lower() == "/shop":
        #Opens the shop
        os.system('cls')
        #Clears cmd
        print("You have opened the shop. Please select an item to purchase!\n")
        #Tells you, you've opened the shop
        while True:
            command = input("Please enter /buy {Item} {Amount} to purchase an item\n\n")
            #How to operate the command
            if len(command.split()) > 3:
                os.system('cls')
                print("Please enter less than 4 parameters!\n")
            elif len(command.split()) < 3:
                #if missing 3rd argument
                os.system('cls')
                #Clears cmd
                print("Plese enter an amount you want to buy!\n")
                #tells you, you needed to buy an amount something {Amount}
            elif command.lower().startswith("/buy copper"):
                os.system('cls')
                args = command.split()
                try:
                    print(f"You have spent ${int(args[2]) * 100} on Copper\n")
                except ValueError:
                    print("Please provide a numerical value!\n")
                #Prints what is in the Dictionary for copper
            elif command.lower().startswith("/buy iron"):
                os.system('cls')
                args = command.split()
                try:
                    print(f"You have spent ${int(args[2]) * 200} on Iron\n")
                except ValueError:
                    print("Please provide a numerical value!\n")
                #Prints what is in the Dictionary for Iron
            elif command.lower().startswith("/buy gold"):
                os.system('cls')
                args = command.split()
                try:
                    print(f"You have spent ${int(args[2]) * 300} on Gold\n")
                except ValueError:
                    print("Please provide a numerical value!\n")
                #Prints what is in the Dictionary for Gold
            elif command.lower() == "/buy":
                os.system('cls')
                print(f"Please provide a valid item to {command}\n")
                #Prints when missing object to /buy
            else:
                print(f"{command} is not a valid command")
    else:
        print(f"{command} is not a valid command")
        #Shop Commands
