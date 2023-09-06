class ATM:
    def __init__(self):
        self.users = {}  # Store user IDs and PINs
        self.transactions = []  # Store transaction history
        self.current_user = None

    def add_user(self, user_id, pin):
        self.users[user_id] = pin

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id] == pin:
            self.current_user = user_id
            return True
        else:
            return False

    def display_menu(self):
        print("\nATM Menu:")
        print("1) Transaction History")
        print("2) Withdraw")
        print("3) Deposit")
        print("4) Transfer")
        print("5) Quit")

    def perform_transaction(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_transaction_history()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def show_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

    def withdraw(self):
        amount = float(input("Enter the withdrawal amount: "))
        if amount > 0:
            self.transactions.append(f"Withdrew ${amount}")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def deposit(self):
        amount = float(input("Enter the deposit amount: "))
        if amount > 0:
            self.transactions.append(f"Deposited ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def transfer(self):
        target_user = input("Enter the target user ID: ")
        if target_user in self.users and target_user != self.current_user:
            amount = float(input("Enter the transfer amount: "))
            if amount > 0:
                self.transactions.append(f"Transferred ${amount} to {target_user}")
                print(f"${amount} transferred to {target_user} successfully.")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Invalid target user ID.")

if __name__ == "__main__":
    atm = ATM()

    # Add some sample users
    atm.add_user("user1", "1234")
    atm.add_user("user2", "5678")

    # Authenticate user
    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")

    if atm.authenticate_user(user_id, pin):
        print(f"Welcome, {user_id}!")
        atm.perform_transaction()
    else:
        print("Authentication failed. Invalid user ID or PIN.")
