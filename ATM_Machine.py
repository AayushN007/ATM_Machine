# ATM Machine Program

balance = 10000
correct_pin = 1234

print("WELCOME TO ATM")

card = input("Insert card (yes/no): ")

if card.lower() == "yes":

    pin = int(input("Enter 4 digit PIN: "))

    if pin == correct_pin:

        print("\nSelect Language")
        print("1. English")
        print("2. Hindi")
        print("3. Kannada")

        lang = int(input("Enter choice: "))

        print("\nSelect Options")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance Enquiry")

        option = int(input("Enter option: "))

        if option == 1:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                print("Please wait...")
                balance = balance - amount
                print("Collect cash")
                print("Transaction Successful")
            else:
                print("Insufficient Balance")

        elif option == 2:
            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount
            print("Please wait...")
            print("Deposit Successful")

        elif option == 3:
            print("Your balance is:", balance)

        else:
            print("Invalid option")

        print("\nDo you want balance?")
        print("1. Yes")
        print("2. No")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Balance:", balance)

        print("Thank you")
        print("Visit Again")

    else:
        print("Wrong PIN")

else:
    print("Please insert card")
