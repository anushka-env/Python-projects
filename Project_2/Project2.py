#ATM SIMULATOR

print("=" * 30)
print("   WELCOME TO PYTHON ATM")
print("=" * 30)
attempt = 0
balance = 1000
while attempt < 3:
    pin = int(input("Enter PIN: "))
    if  pin == 1234:
        while True: 
            print("\n ---ATM MENU--- ")
            print("1.Check Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            ch = int(input("Enter your choice: "))
            if  ch==1:
                print("\nBalance is: ",balance)
            elif  ch==2:
                amt = int(input("Enter amount: "))
                if amt>0:
                    print(amt ," deposited successfuly")
                    balance += amt
                    print("\nCurrent balance: ",balance)
                else:
                    print("Invalid amount")
            elif  ch == 3:
                withdraw = int(input("Enter amount: "))
                if withdraw <= 0:
                    print("Invalid amount")
                elif withdraw <= balance:
                    balance = (balance - withdraw)
                    print("\nRemaining balance: ",balance)
                else:
                    print("Insufficient amount..withdrawl not possible")
            elif  ch == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice....")
        break
    else:
        attempt += 1
        print("Wrong PIN")
if attempt == 3:
    print("No more attempts left..access denied")








