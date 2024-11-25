class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than 0.")
    
def display_menu():
    print("\n===== Bank Account Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    # Create a bank account
    account_holder = input("Enter account holder's name: ")
    account = BankAccount(account_holder)
    
    while True:
        display_menu()
        choice = input("Please choose an option (1-4): ")
        
        if choice == "1":
            account.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()

