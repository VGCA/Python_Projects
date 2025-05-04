def show_balance():

    print(f"Your balance is {balance:.2f}")

def deposit():

    amount = float(input("Enter the amount: "))
    return amount

def withdraw():

    amount = float(input("Enter the amount: "))
    if(amount>balance):
        print("You can not withdraw that money from your account")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice=="1":
        show_balance()
    elif choice=="2":
        balance += deposit()
        print("Operation completed")
    elif choice=="3":
        balance -= withdraw()
        print("Operation completed")
    elif choice=="4":
        is_running = False
    else:
        print("Wrong number")

print("Have a nice day")