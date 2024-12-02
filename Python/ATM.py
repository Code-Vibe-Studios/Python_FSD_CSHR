def authenticate(account):
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter the pin: ")
        if entered_pin == account.pin:
            print("Access granted")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN, you have {attempts} attempts remaining")
    print("Too many incorrect attempts. Access denied")
    return False


class Account:
    def __init__(self,accNumber, pin, balance = 0):
        self.accNumber = accNumber
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
        self.transaction_history.append("Checked balance")

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. Current balance: {self.balance}")

    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount}. Current balance: {self.balance}")

    def show_transactions(self):
        if not self.transaction_history:
            print("No transactions found")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)



def atm_menu(account):
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Show Transactions")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid Option. Please try again.")


def main():
    print("Welcome to the ATM!!")
    account = Account("1234567", "1234",10000)
    #Authenticate the User
    if authenticate(account):
        atm_menu(account)
    else:
        print("Exiting the ATM system due to failed authentication")

main()