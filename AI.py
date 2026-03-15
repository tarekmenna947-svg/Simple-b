class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: ${amount}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds!")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew: ${amount}")

    def display_balance(self):
        print("-" * 30)
        print(f"Account Holder: {self.holder}")
        print(f"Current Balance: ${self.balance}")
        print("-" * 30)

def main():
    print("=== Welcome to Simple Bank System ===")
    name = input("Enter your name to open an account: ")
    user_account = BankAccount(name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            try:
                amt = float(input("Enter amount to deposit: "))
                user_account.deposit(amt)
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == '2':
            try:
                amt = float(input("Enter amount to withdraw: "))
                user_account.withdraw(amt)
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        elif choice == '3':
            user_account.display_balance()
            
        elif choice == '4':
            print("Thank you for using our bank. Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
    
