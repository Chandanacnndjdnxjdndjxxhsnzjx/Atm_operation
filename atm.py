atm_pin = 5693
account_balance = 10000

user_input1 = int(input("Please enter the ATM pin: "))
if user_input1 == atm_pin:
    user_input = input(
        """Press 1 for withdrawal, press 2 for balance check, press 3 for deposit, press 4 for main menu: """
    )
    if user_input == "1":
        withdraw_amount = int(input("Enter the amount: "))
        if withdraw_amount <= account_balance:
            account_balance -= withdraw_amount
            print(f"Please collect the cash: {withdraw_amount}")
            print(f"Remaining balance: {account_balance}")
        else:
            print("Insufficient balance.")
    elif user_input == "2":
        print(f"Your account balance is {account_balance}.")
    elif user_input == "3":
        deposit_amount = int(input("Please enter the amount you want to deposit: "))
        account_balance += deposit_amount
        print("Amount is deposited.")
        print(f"Updated balance: {account_balance}")
    elif user_input == "4":
        print("Returning to the main menu...")
    else:
        print("Invalid option selected.")
else:
    print("Invalid pin.")
