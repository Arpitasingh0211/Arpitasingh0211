def deposite():
    amount = int(input("Enter an amount to be deposited = "))
    if amount < 0:
        print("This is not a valid amount")
    else:
        return amount    
    
def withdraw():
    amount = int(input("Enter an amount to be withdraw = "))
    if amount < 0:
        print("This is not a valid amount")
    else:
        return amount
    
def showBalance():
    print(f"Your current balance is {balance}")

       
balance = 0                      
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4) = ")     

    if choice == "1":
        showBalance()

    elif choice == "2" :
        balance += deposite()
        showBalance()

    elif choice == "3" :
        balance -= withdraw()
        showBalance()

    elif choice == "4" :
        is_running = False

    else:
        print("That is not a valid choise")    

print("Thank You!!! Have a nice day ")
